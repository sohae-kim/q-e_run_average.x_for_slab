#!/usr/bin/python
import os
import stat
from numpy import mean

def pot_avg(scfi,scfo):
    
    outavg = open("avg.in",'w')
    outavg.write("1		#\npotential \n1.D0 		#\n")
    inscfo = open(scfo)
    for line in inscfo:
        if line.startswith("     Smooth"):
            tmp = line.split()
            tmp1= tmp[9].split(")")
            outavg.write(tmp1[0]+"0 		# ~10*(number of FFT grid points in z from scf.out)\n3 		# direction (z) along which you want the potential\n")
 
    inscfi = open(scfi)
    flag=0
    z=[]
    zavg=[]
    for line in inscfi:
        if line.startswith("ATOMIC_POSITIONS"):flag=1
        elif line.startswith("K_POINTS"):flag=0
        if flag==1:
            if line.startswith("Ti"):
                tmp = line.split()
                znew= float(tmp[3])
                #print znew
                if not z or abs(mean(z)-znew) < 1.5: z.append(znew) #if z is empty or on the same plane
                else: 
                    #print mean(z)
                    zavg.append(mean(z))
                    z[:]=[]
                    z.append(znew)

    #print zavg
    dz=[]
    for i in range(len(zavg)-1): dz.append(zavg[i+1]-zavg[i])
    print "Average dz of Ti = ",mean(dz)
    outavg.write(str(mean(dz))+"             # averaging window along z = average lattice spacing along z")

for file in os.listdir("./"):
    if file.endswith(".scf.in"):
        print(file)
        scfi=file
    if file.endswith(".scf.out"):
        print(file)
        scfo=file
 
pot_avg(scfi,scfo)
print ("1_pot_avg.py: done")

