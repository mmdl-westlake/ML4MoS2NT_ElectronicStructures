##created by Ju Huang: huangju33@gamil.com
##used for create KPOINTS files by loading "info_A_B_set.csv"
import os
import pandas as pd

df = pd.read_csv('info_A_B_set.csv')

for index, row in df.iterrows():
    n = row['n']
    m = row['m']
    x_A = row['x_A']
    y_A = row['y_A'] 
    x_B = row['x_B']
    y_B = row['y_B'] 
    u = row['u']
    N = row['N']

    dir_name = f'mos2_{n}_{m}'
    os.makedirs(dir_name, exist_ok=True)

    subdir_name = os.path.join(dir_name, f'u_{u}_N_{N}')
    os.makedirs(subdir_name, exist_ok=True)
    kpoints_content = f"""k-points along high symmetry lines
80  !80 intersections
Line-mode
reciprocal
{x_A} {y_A} 0 !A
{x_B} {y_B} 0 !B
"""
    with open(os.path.join(subdir_name, 'KPOINTS'), 'w') as kpoints_file:
        kpoints_file.write(kpoints_content)

print("Directories, subdirectories, and KPOINTS files created successfully.")
