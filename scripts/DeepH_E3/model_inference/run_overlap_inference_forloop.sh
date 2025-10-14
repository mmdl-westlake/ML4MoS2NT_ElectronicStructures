#!/bin/bash
#SBATCH -p cp6
#SBATCH -N 4
#SBATCH -n 224
#SBATCH --output overlap_inference.out
#SBATCH -J overlap_inference
#SBATCH --error error.out


base_directory=$(pwd)

# Loop through all directories matching mos2_*_*
for i in mos2_*_*; do
    cd "$i"
    start_time=$(date +%s)
    echo "overlap&inference $i started at: $(date)"

    #refined_fermi_energy=$(jq 'refined_fermi_energy' band.json)
    #refined_fermi_energy=$(python -c "import json; print(json.load(open('band.json'))['refined_fermi_energy'])")

    mkdir -p overlap
    cp /fs2/home/huangju/deeph_e3/full_structural_relaxation/n_m_in_54_80_EffMass/n_m/poscar2openmx_soc.py .
    python poscar2openmx_soc.py
    cp openmx_in.dat overlap/openmx_in.dat
    cd overlap

    mkdir inference
    cd inference

    cat > inference.ini <<EOF
[basic]
OLP_dir = $base_directory/$i/overlap
work_dir = $base_directory/$i/overlap/inference
device = cpu
interface = openmx
task = [1]
sparse_calc_config = $base_directory/$i/overlap/inference/inference_band/band.json

restore_blocks_py = True
eigen_solver = sparse_jl

[interpreter]
julia_interpreter = julia

[graph]
radius = -1.0
create_from_DFT = True
EOF

    mkdir inference_band
    cd inference_band

    cat > band.json <<EOF
{
  "calc_job": "band",
  "which_k": 0,
  "fermi_level": -5.0,
  "max_iter": 300,
  "num_band": 100,
  "k_data": ["100 0 0 0 0 0.5 0  Γ Z"]
}
EOF

    cd ../..

    module purge
    module load openmx/3.9-overlap-icc19-openmpi

    mkdir -p output
    srun openmx openmx_in.dat > openmx.std

    sleep 5

    module purge
    cd ./inference/

    source activate deeph
    module load hdf5/1.12.0-icc19.0-openmpi

    deeph-inference --config inference.ini
    echo "overlap&inference $i ended at: $(date)"

    cpus=$(grep -oP '#SBATCH -n \K\d+' "$0")
    echo "CPUs used for $i: $cpus"

    nodes=$(grep -oP '#SBATCH -N \K\d+' "$0")
    echo "nodes used for $i: $nodes"

    #cd ../../..
    cd $base_directory
done

