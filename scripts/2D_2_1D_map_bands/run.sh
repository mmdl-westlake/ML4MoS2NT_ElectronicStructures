#!/bin/bash
##SBATCH --job-name=vasp
#SBATCH --partition=cp6
#SBATCH -N 2
#SBATCH -n 112
#SBATCH --output=vasp.out
#SBATCH --error=vasp.err


module purge  
module use --append /fs2/home/liwenbin/.privatemodules
module add vasp

yhrun  vasp_ncl

