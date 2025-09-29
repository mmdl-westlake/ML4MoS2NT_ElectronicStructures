#!/bin/bash

for i in $(seq 50 69); do
    formatted_num=$(printf "%.1f" "$i")
    for dir in u_${formatted_num}_N_*; do
        if [ -d "$dir" ]; then
            echo "Entering directory $dir"
            cd "$dir"
	        cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/CHG .
	        cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/CHGCAR .
            cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/INCAR .
            cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/POSCAR .
            cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/POTCAR .
            cp /fs2/home/huangju/vasp/full_structural_relaxation/remap_band_total_16/run.sh .
            
	        sbatch run.sh

            
            cd ..

            echo "Exiting directory $dir"
        fi
    done
done

