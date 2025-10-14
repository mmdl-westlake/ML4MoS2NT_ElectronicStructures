#!/bin/bash
#SBATCH -p cp6
#SBATCH -N 4
#SBATCH -n 224
#SBATCH -J E_B
#SBATCH --error e3_error.out
#SBATCH --output e3_pred_band.out

start_time=$(date +%s)
echo "e3_band prediction started at: $(date)"


source activate deeph-gpu
module purge
#module load hdf5/1.12.0-icc19.0-openmpi


export PATH=/fs2/home/huangju/software/DeepH-E3/:$PATH

cp /fs2/home/huangju/deeph_e3/full_structural_relaxation/production_run/sparse_calc_deeph.jl sparse_calc_deeph.jl
cp /fs2/home/huangju/deeph_e3/full_structural_relaxation/production_run/eval_default.ini eval_default.ini

mkdir -p graph
mkdir -p deeph-e3_mixed

deephe3-eval.py eval_default.ini

cp ./inference/inference_band/band.json band.json

cd ./inference
cp ./inference/hamiltonians_pred.h5 hamiltonians_pred.h5
cp ./inference/info.json info.json
cd ../


julia sparse_calc_deeph.jl -i inference -o deeph-e3_mixed --config band.json

cd deeph-e3_mixed
mkdir -p compare_bands
cp /fs2/home/huangju/deeph_e3/add_relaxation_study/test_set/plot_band_scatter_each_k.py plot_band_scatter_each_k.py
python plot_band_scatter_each_k.py -t openmx -f png -i 200 -d -2 -u 2

end_time=$(date +%s)
echo "e3_band prediction ended at: $(date)"
elapsed_time=$((end_time - start_time))
echo "Total time for the calculation: $elapsed_time seconds"


cpus=$(grep -oP '#SBATCH -n \K\d+' "$0")
echo "CPUs used: $cpus"
nodes=$(grep -oP '#SBATCH -N \K\d+' "$0")
echo "nodes used: $nodes"
