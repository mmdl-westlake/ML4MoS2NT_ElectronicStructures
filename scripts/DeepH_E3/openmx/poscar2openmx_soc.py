### this poscar2openmx_soc.py is used to convert the POSCAR file of MoS2 to the openmx input file with SOC
### the orbital information of atoms should be modified to your systems
### code written by Ju Huang, email: huangju33@gmail.com
import os
import sys

import numpy as np
from pymatgen.core.structure import Structure

current_directory = os.getcwd()

poscar_path = os.path.join(current_directory, 'POSCAR')

mos2_poscar = Structure.from_file(poscar_path)
species = mos2_poscar.species
frac_coords = mos2_poscar.frac_coords
cart_coords = mos2_poscar.cart_coords
lattice_vectors = mos2_poscar.lattice.matrix
num_atoms = len(species)

atom_lines =""
for i, (specie, coord) in enumerate(zip(species, frac_coords), start = 1):
    if specie.symbol == "Mo":
        values = "7.0 7.0 0.0 0.0 0.0 0.0 0"
    elif specie.symbol == "S":
        values = "3.0 3.0 0.0 0.0 0.0 0.0 0"
    else:
        values = "0.0 0.0 0.0 0.0 0.0 0.0 0"

    atom_line = f'{i} {specie.symbol} {coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f} {values}'
    if i < num_atoms:
        atom_line +="\n"
    atom_lines += atom_line



header = f"""system.name openmx
DATA.PATH           /fs2/home/huangju/software/openmx3.9/DFT_DATA19
HS.fileout                        on

Species.Number       2
<Definition.of.Atomic.Species
Mo   Mo7.0-s3p2d2       Mo_PBE19
S   S7.0-s2p2d1       S_PBE19
Definition.of.Atomic.Species>

#
# Atoms
#
Atoms.Number          {num_atoms}
Atoms.SpeciesAndCoordinates.Unit FRAC

<Atoms.SpeciesAndCoordinates
{atom_lines}
Atoms.SpeciesAndCoordinates>


Atoms.UnitVectors.Unit             Ang #  Ang|AU
<Atoms.UnitVectors                     # unit=Ang.
{lattice_vectors[0][0]:.6f}   {lattice_vectors[0][1]:.6f}   {lattice_vectors[0][2]:.6f}
{lattice_vectors[1][0]:.6f}   {lattice_vectors[1][1]:.6f}   {lattice_vectors[1][2]:.6f}
{lattice_vectors[2][0]:.6f}   {lattice_vectors[2][1]:.6f}   {lattice_vectors[2][2]:.6f}
Atoms.UnitVectors>

scf.XcType                        GGA-PBE   # LDA/LSDA-CA/LSDA-PW/GGA-PBE
scf.ElectronicTemperature         300.0     # default=300 (K) SIGMA in VASP
scf.energycutoff                  300       # default=150 (Ry = 13.6eV)
scf.maxIter                       2000
scf.EigenvalueSolver              Band      # DC/DC-LNO/Krylov/ON2/Cluster/Band
scf.Kgrid                         1  5  1
scf.criterion                     4e-08     # (Hartree = 27.21eV)
scf.partialCoreCorrection         on

scf.SpinPolarization              nc
scf.SpinOrbit.Coupling            on

scf.Mixing.Type                   RMM-DIISK
scf.Init.Mixing.Weight            0.3
scf.Mixing.History                30
scf.Mixing.StartPulay             6
scf.Mixing.EveryPulay             1

1DFFT.EnergyCutoff                3600
1DFFT.NumGridK                    900
1DFFT.NumGridR                    900

scf.ProExpn.VNA                   off

MD.Type                         Nomd      # Nomd (SCF) / NVT_NH (MD)

Band.dispersion                 on
Band.Nkpath                     1
<Band.kpath
20 0 0 0  0 0.5 0  \Gamma Z
Band.kpath>
### END ###
"""
footer = """ 
"""

save_str = header + footer

output_path = os.path.join(current_directory, "openmx_in.dat")

with open (output_path, 'w') as save_f:
    save_f.write(save_str)
