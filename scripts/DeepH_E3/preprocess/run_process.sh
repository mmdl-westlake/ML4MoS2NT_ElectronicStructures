#!/bin/bash
#SBATCH -p cp6
#SBATCH -N 2
#SBATCH -n 112
#SBATCH --output preprocess.out
#SBATCH --error error.out


source activate deeph

module purge 
export PATH="/fs2/home/huangju/software/DeepH-E3/:$PATH"


directories=("n_m")

for dir in "${directories[@]}"; do

    echo "preprocess $dir started at: $(date)"
    deephe3-preprocess.py "preprocess_${dir}.ini"

    echo "preprocess $dir ended at: $(date)"
    sleep 5
done



cpus=$(grep -oP '#SBATCH -n \K\d+' "$0")

echo "CPUs used: $cpus"

nodes=$(grep -oP '#SBATCH -N \K\d+' "$0")

echo "nodes used: $nodes"


