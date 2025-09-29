#!/bin/bash
#SBATCH -N 1
#SBATCH --partition qgpu_4090
#SBATCH --cpus-per-gpu=8
#SBATCH --gres=gpu:1
#SBATCH --mem=100GB
#SBATCH -J deeph-e3
#SBATCH --error error.out
#SBATCH --output train.out


source activate deeph-gpu

start_time=$(date +%s)

echo "train started at: $(date)"

nvidia-smi dmon -d 5 -s um -o T > nvi_5.log &
export PATH=/hpcfs/fhome/liwenbin/wenlab_work/software/DeepH-E3/:$PATH

deephe3-train.py train.ini

echo "train ended at: $(date)"
nodes=$(grep -oP '#SBATCH -N \K\d+' "$0")
echo "nodes used for train: $nodes"

