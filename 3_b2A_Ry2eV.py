#!/usr/bin/python
import os
import stat
from numpy import mean

def b2A_Ry2eV(scfi,scfo,avgo):
    
    outmcr = open("elspot-macro_avg.dat",'w')
    outpln = open("elspot-planar_avg.dat",'w')
    outmcr.write("# z [A]         Electrostatic potential [eV]\n")
    outpln.write("# z [A]         Electrostatic potential [eV]\n")

    inscfo = open(scfo)
    for line in inscfo:
        if line.startswith("     the Fermi energy is"): 
            tmp = line.split()
            Ef = float(tmp[4])
 
    inscfi = open(scfi)
    flag=0
    z=[]
    for line in inscfi:
        #print line, flag
        if line.startswith("Ti") and (flag ==0 or flag == 1): 
            #print line
            tmp = line.split()
            #print tmp
            z.append(float(tmp[3]))
            flag = 1
        elif line.startswith("O") and flag ==1: flag=2
    #print z
    zTi = mean(z)        

    inavgo = open(avgo)
    flag=0
    for line in inavgo:
        if line.startswith("\n"): flag=0
        elif flag == 1:
            tmp = line.split()
            #print tmp
            z = (float(tmp[0])-zTi)*0.5292
            pot_mcr = float(tmp[2])*13.6058-Ef
            pot_pln = float(tmp[1])*13.6058-Ef
            outmcr.write(str(z)+"    "+str(pot_mcr)+"\n")
            outpln.write(str(z)+"    "+str(pot_pln)+"\n")
        if line.startswith("     Reading data"): flag=1
              
for file in os.listdir("./"):
    if file.endswith("avg.out"):
        print(file)
        avgo=file
    if file.endswith(".scf.out"):
        print(file)
        scfo=file
    if file.endswith(".scf.in"):
        print(file)
        scfi=file

b2A_Ry2eV(scfi,scfo,avgo)
print ("3_b2A_Ry2eV.py: done")

