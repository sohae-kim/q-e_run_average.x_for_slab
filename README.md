# q-e_pp
## Run 1_pot_avg.py, 2_run_avg and 3_b2A_Ry2eV.py in order.

## 1_pot_avg.py 
* Input: sci.in & sci.out 
* Output: avg.in that will be used as an input file for average.x 
* What it does: 
	1) Calculate averaging window along z = average lattice spacing along z. Specifically in this example, find the interfacial Ti atom and the next Ti along z (lattice constant c, or 1/4 lattice constant c in case of anatase)
	2) Calculate ~10*(number of FFT grid points in z from scf.out). Maximum for average.x is set to 5000? 6000? (need to check and to be added to max limit)
	3) Write the avg.in file based on the calculations

## 2_run_avg 
* Input: avg.in that was generated from the previous step 
* Output: avg.out with the last 3 lines trimmed for the next step 
* What it does: 
	1) Run average.x with the input file, avg.in 
	2) Write the output in avg.out 
	3) Trim the last 3 lines for the next step

## 3_b2A_Ry2eV.py 
* Input: avg.out, sci.in & sci.out 
* Output: elspot-macro_avg.dat & elspot-planar_avg.dat 
* What it does:
	1) Find Fermi level from sci.out and Find the z position of the interfacial Ti from sci.in
	2) From the avg.out, convert the units of z from bohr to Å, set the z position of the interfacial Ti as zero, and shift the electrostatic potential relative to the Fermi energy level.
	3) Write the output in different files of elspot-macro_avg.dat & elspot-planar_avg.dat for averaged & not-averaged potentials, respectively.
