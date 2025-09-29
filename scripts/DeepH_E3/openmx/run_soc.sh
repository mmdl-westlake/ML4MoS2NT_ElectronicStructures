#!/bin/bash

#SBATCH -p cp6
#SBATCH -N 2
#SBATCH -n 112
#SBATCH -J openmx

source activate deeph
module purge
module load openmx/3.9-icc19-openmpi


python poscar2openmx_soc.py
srun openmx openmx_in.dat > openmx.std
cat openmx.out >> openmx.scfout
rm -r openmx_rst *.cube
