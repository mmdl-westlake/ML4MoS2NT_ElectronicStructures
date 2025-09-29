###Created by Ju Huang: huangju33@gmail.com
###load fine tuned CHGNet model for application
from chgnet.model import StructOptimizer
from pymatgen.core import Structure
from ase.io import Trajectory, write
from chgnet.model import CHGNet

chgnet = CHGNet.from_file('/fs2/home/huangju/chgnet/with_full_relaxation/FineTuning_model_vasp_mix_aimd_relaxation/mos2_test_dataset/epoch99_e0_f9_s4_mNA.pth.tar')

structure = Structure.from_file('POSCAR')

relaxer = StructOptimizer(model=chgnet)

result = relaxer.relax(atoms=structure, fmax=0.005, steps=2000)

traj = result['trajectory']

e = traj.compute_energy()   # eV/cell
with open('chgnet_energy.tote', mode='w') as f:
    f.write(str(e))

opt_struc = result["final_structure"]
opt_struc.to(fmt='poscar', filename='chgnet_CONTCAR')

struc = Structure.from_file('chgnet_CONTCAR')

prediction = chgnet.predict_structure(struc)

print(f"Prediction keys: {prediction.keys()}")

print(f"Prediction content: {prediction}")

with open("CHGNet_energy.dat", 'w') as energy_file:
    energy_file.write(f"CHGNet-predicted energy (eV/atom):\n{prediction['e']}\n")

with open("CHGNet_force.dat", 'w') as forces_file:
    forces_file.write(f"CHGNet-predicted forces (eV/A):\n")
    for force in prediction['f']:
        forces_file.write(" ".join(map(str, force)) + "\n")

print("Predicted energy saved to CHGNet_energy.dat")
print("Predicted forces saved to CHGNet_force.dat")

