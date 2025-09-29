from vasppy.rdf import RadialDistributionFunction
from pymatgen.core import Structure, Lattice
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm


arial_path = '/fs2/home/huangju/software/miniconda3/envs/deeph/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/arial.ttf'

if not os.path.exists(arial_path):
    raise FileNotFoundError(f"Font file not found at {arial_path}")

fm.fontManager.addfont(arial_path)

arial_font = fm.FontProperties(fname=arial_path)

plt.rcParams['font.family'] = arial_font.get_name()

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=SMALL_SIZE)
plt.rc('axes', labelsize=SMALL_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.rc('axes', linewidth=1)
plt.rc('figure', figsize=(3.33,0.75*3.33))
#plt.rc('figure', dpi=600)


struc_chgnet = Structure.from_file('chgnet_CONTCAR')

struc_unrelax = Structure.from_file('POSCAR')


rdf_chgnet = RadialDistributionFunction.from_species_strings(structures=[struc_chgnet], species_i='Mo', species_j='S')

rdf_unrelax = RadialDistributionFunction.from_species_strings(structures=[struc_unrelax], species_i='Mo', species_j='S')

plt.plot(rdf_chgnet.r, rdf_chgnet.smeared_rdf(), label='CHGNet Mo-S', c='tab:orange', zorder=2)
plt.plot(rdf_unrelax.r, rdf_unrelax.smeared_rdf(), label='Unrelax Mo-S', c='tab:grey', linestyle='-', zorder=1)

plt.xlabel(r"Bond Distance ($\mathrm{\AA}$)")
plt.ylabel(r"Radial Distribution Function ($\mathrm{\AA}^{-3}$)")
plt.legend()
plt.tight_layout()
plt.savefig('rdf.png',dpi=200)
