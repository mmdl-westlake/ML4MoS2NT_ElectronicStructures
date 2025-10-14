###Created by Ju Huang: huangju33@gmail.com
###followed with https://github.com/CederGroupHub/chgnet/blob/main/examples/fine_tuning.ipynb
for fine tune chgnet for MoS2 nanotube
from pathlib import Path
import numpy as np
from pymatgen.core import Structure, Lattice
from chgnet.data.dataset import StructureData, get_train_val_test_loader
from chgnet.trainer import Trainer
from chgnet.model import CHGNet
from chgnet.utils import read_json
from chgnet.utils import parse_vasp_dir
import os
import json
from chgnet.graph import CrystalGraph, CrystalGraphConverter

combined_json_path = "./combined_chgnet_dataset.json"

with open(combined_json_path, 'r') as infile:
    combined_dataset_dict = json.load(infile)

structures = [Structure.from_dict(struct) for struct in combined_dataset_dict["structure"]]
energies = combined_dataset_dict["energy_per_atom"]
forces = combined_dataset_dict["force"]
stresses = None if combined_dataset_dict["stress"] in [None, []] else combined_dataset_dict["stress"]
magmoms = None if combined_dataset_dict["magmom"] in [None, []] else combined_dataset_dict["magmom"]

dataset = StructureData(
    structures=structures,
    energies=energies,
    forces=forces,
    stresses=stresses,
    magmoms=magmoms,
)

train_loader, val_loader, test_loader = get_train_val_test_loader(
    dataset,
    batch_size=8,
    train_ratio=0.9,
    val_ratio=0.05
)

train_test_split = {
    "train_loader": train_loader,
    "test_loader": test_loader,
    "val_loader": val_loader
}

train_indices = getattr(train_loader.dataset, 'indices', None)
val_indices = getattr(val_loader.dataset, 'indices', None)
test_indices = getattr(test_loader.dataset, 'indices', None)

def create_data_dict(indices):
    data_dict = {}
    for key in combined_dataset_dict:
        value_list = combined_dataset_dict[key]
        if value_list is not None:
            try:
                data_dict[key] = [value_list[i] for i in indices]
            except Exception as e:
                print(f"Error processing key '{key}': {e}")
                data_dict[key] = None
        else:
            data_dict[key] = None
    return data_dict

if train_indices is not None:
    train_data_dict = create_data_dict(train_indices)
    with open('train_data.json', 'w') as f:
        json.dump(train_data_dict, f)
else:
    print("Train indices not found.")

if val_indices is not None:
    val_data_dict = create_data_dict(val_indices)
    with open('val_data.json', 'w') as f:
        json.dump(val_data_dict, f)
else:
    print("Validation indices not found.")

if test_indices is not None:
    test_data_dict = create_data_dict(test_indices)
    with open('test_data.json', 'w') as f:
        json.dump(test_data_dict, f)
else:
    print("Test indices not found.")

if train_indices is not None:
    print(f"Number of structures in train_data.json: {len(train_data_dict['structure'])}")
if val_indices is not None:
    print(f"Number of structures in val_data.json: {len(val_data_dict['structure'])}")
if test_indices is not None:
    print(f"Number of structures in test_data.json: {len(test_data_dict['structure'])}")

chgnet = CHGNet.load()

for layer in [
    chgnet.atom_embedding,
    chgnet.bond_embedding,
    chgnet.angle_embedding,
    chgnet.bond_basis_expansion,
    chgnet.angle_basis_expansion,
    chgnet.atom_conv_layers[:-1],
    chgnet.bond_conv_layers,
    chgnet.angle_layers,
]:
    for param in layer.parameters():
        param.requires_grad = False

trainer = Trainer(
    model=chgnet,
    targets="efs",
    energy_loss_ratio=1,
    force_loss_ratio=1,
    stress_loss_ratio=0.1,
    optimizer="Adam",
    scheduler="CosLR",
    scheduler_params={'decay_fraction': 0.5e-2},
    criterion="MSE",
    delta=0.1,
    epochs=100,
    learning_rate=1e-3,
    use_device="cpu",
    print_freq=100,
)

trainer.train(train_loader, val_loader, test_loader)
