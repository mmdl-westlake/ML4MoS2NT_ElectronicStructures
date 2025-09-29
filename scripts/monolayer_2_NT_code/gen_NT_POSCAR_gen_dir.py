### python code from JuHuang; email: huangju33@gmail.com
### input poscar is the monolayer, chiral_index.txt is needed with (n,m) sets, change below the related parameters to get the reciprocal lattice vectors for your system of 2H or 1T phase.
### this code is followed by the matlab code from Prof. Wenbin Li
### python version of: Python 3.12.2
import numpy as np
import os

def read_poscar(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    scaling_factor = float(lines[1].strip())
    lattice_vectors = np.array([list(map(float, lines[i].split())) for i in range(2, 5)]) * scaling_factor
    element_symbols = lines[5].split()
    element_counts = list(map(int, lines[6].split()))

    atomic_coordinates = []
    current_index = 8
    for count in element_counts:
        for i in range(count):
            atomic_coordinates.append(list(map(float, lines[current_index].split()[:3])))
            current_index += 1

    atomic_coordinates = np.array(atomic_coordinates)
    element_positions = {}
    index = 0
    for symbol, count in zip(element_symbols, element_counts):
        element_positions[symbol] = atomic_coordinates[index:index + count]
        index += count

    return lattice_vectors, element_positions

def calculate_thickness(element_positions, lattice_vectors):
    S_positions = element_positions['S']
    z_positions = S_positions[:, 2] * lattice_vectors[2][2]
    d0 = np.max(z_positions) - np.min(z_positions)
    return d0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fractional_to_cartesian(fractional_coords, lattice_vectors):
    return fractional_coords @ lattice_vectors

def generate_nanotube_from_poscar(poscar_file, chiral_vec, vacuum_layer, fsave_name):
    lattice_vectors, element_positions = read_poscar(poscar_file)
    d0 = calculate_thickness(element_positions, lattice_vectors)
    n, m = chiral_vec

    a0 = 3.184 ### lattice of mos2 monolayer
    a1 = a0 * np.array([np.sqrt(3)/2, -0.5])
    a2 = a0 * np.array([np.sqrt(3)/2, 0.5])

    mot_2D_M = np.array([0.0, 0.0])
    ### 2H phase with below seetings
    mot_2D_X1 = (1/3) * a1 + (1/3) * a2
    mot_2D_X2 = (1/3) * a1 + (1/3) * a2
    ### 1T phase with below settings
    #mot_2D_X1 = (1/3) * a1 + (1/3) * a2
    #mot_2D_X2 = (2/3) * a1 + (-1/3) * a2
    mot_3D_M = np.array([0.0, 0.0, 0.0])
    mot_3D_X1 = np.array([*mot_2D_X1, d0/2])
    mot_3D_X2 = np.array([*mot_2D_X2, -d0/2])

    C = m * a1 + n * a2
    t1 = -(2 * n + m)
    t2 = 2 * m + n
    common_divisor = gcd(2 * m + n, 2 * n + m)
    T = (t1 * a1 + t2 * a2) / common_divisor

    LL_C = np.linalg.norm(C)
    LL_T = np.sqrt(3) * LL_C / common_divisor
    R = LL_C / (2 * np.pi)

    lambda_val = np.linalg.norm(C + T) / np.linalg.norm(a1)
    id_range = int(np.ceil(lambda_val)) * 2

    temp_M, temp_X1, temp_X2 = [], [], []
    for ii in range(-id_range, id_range + 1):
        for jj in range(-id_range, id_range + 1):
            coord_temp_M = mot_2D_M + ii * a1 + jj * a2
            coord_temp_X1 = mot_2D_X1 + ii * a1 + jj * a2
            coord_temp_X2 = mot_2D_X2 + ii * a1 + jj * a2
            temp_M.append(coord_temp_M)
            temp_X1.append(coord_temp_X1)
            temp_X2.append(coord_temp_X2)

    temp_M = np.array(temp_M)
    temp_X1 = np.array(temp_X1)
    temp_X2 = np.array(temp_X2)

    H0 = np.array([C, T]).T

    temp_M_frac = np.linalg.lstsq(H0, temp_M.T, rcond=None)[0].T
    temp_X1_frac = np.linalg.lstsq(H0, temp_X1.T, rcond=None)[0].T
    temp_X2_frac = np.linalg.lstsq(H0, temp_X2.T, rcond=None)[0].T

    tol = 1e-9
    M_indices = np.where((temp_M_frac[:, 0] > -tol) & (temp_M_frac[:, 0] < 1 - tol) &
                         (temp_M_frac[:, 1] > -tol) & (temp_M_frac[:, 1] < 1 - tol))[0]
    X1_indices = np.where((temp_X1_frac[:, 0] > -tol) & (temp_X1_frac[:, 0] < 1 - tol) &
                          (temp_X1_frac[:, 1] > -tol) & (temp_X1_frac[:, 1] < 1 - tol))[0]
    X2_indices = np.where((temp_X2_frac[:, 0] > -tol) & (temp_X2_frac[:, 0] < 1 - tol) &
                          (temp_X2_frac[:, 1] > -tol) & (temp_X2_frac[:, 1] < 1 - tol))[0]

    M_frac = temp_M_frac[M_indices]
    X1_frac = temp_X1_frac[X1_indices]
    X2_frac = temp_X2_frac[X2_indices]

    natom_M = M_frac.shape[0]
    npair_X = X1_frac.shape[0]

    if natom_M != npair_X:
        raise ValueError('The number of M atoms is not equal to the pair of X atoms. Something must be wrong!')

    H0_new = np.array([[LL_C, 0], [0, LL_T]])
    M_cart_2D = M_frac @ H0_new
    X1_cart_2D = X1_frac @ H0_new
    X2_cart_2D = X2_frac @ H0_new

    M_cart_unroll = np.hstack((M_cart_2D, np.zeros((natom_M, 1))))
    X1_cart_unroll = np.hstack((X1_cart_2D, d0 / 2 * np.ones((natom_M, 1))))
    X2_cart_unroll = np.hstack((X2_cart_2D, -d0 / 2 * np.ones((natom_M, 1))))

    R_M = R * np.ones(natom_M)
    theta_M = M_frac[:, 0] * 2 * np.pi
    x_M = R_M * np.sin(theta_M)
    z_M = R_M * (1.0 - np.cos(theta_M))

    R_X1 = R_M - d0 / 2
    theta_X1 = X1_frac[:, 0] * 2 * np.pi
    x_X1 = R_X1 * np.sin(theta_X1)
    z_X1 = R_X1 * (1.0 - np.cos(theta_X1)) + d0 / 2

    R_X2 = R_M + d0 / 2
    theta_X2 = X2_frac[:, 0] * 2 * np.pi
    x_X2 = R_X2 * np.sin(theta_X2)
    z_X2 = R_X2 * (1.0 - np.cos(theta_X2)) - d0 / 2

    M_cart = np.column_stack((x_M, M_cart_unroll[:, 1], z_M))
    X_cart1 = np.column_stack((x_X1, X1_cart_unroll[:, 1], z_X1))
    X_cart2 = np.column_stack((x_X2, X2_cart_unroll[:, 1], z_X2))

    Coord = np.vstack((M_cart, X_cart1, X_cart2))
    CoM = np.mean(Coord, axis=0)

    H1 = np.zeros((3, 3))
    H1[0, 0] = 2 * R + vacuum_layer
    H1[1, 1] = LL_T
    H1[2, 2] = 2 * R + vacuum_layer

    shift = np.array([H1[0, 0] / 2 - CoM[0], 0, H1[2, 2] / 2 - CoM[2]])
    M_cart += shift
    X_cart1 += shift
    X_cart2 += shift

    inv_H1 = np.linalg.inv(H1)
    M_frac_final = M_cart @ inv_H1
    X_frac1_final = X_cart1 @ inv_H1
    X_frac2_final = X_cart2 @ inv_H1


    base_dir = f"mos2_{n}_{m}"
    nt_dir = os.path.join(base_dir, "NT")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    if not os.path.exists(nt_dir):
        os.makedirs(nt_dir)

    filename = os.path.join(nt_dir, f"{fsave_name}_NT_POSCAR")
    write_poscar(H1, ['Mo', 'S'], natom_M, npair_X, M_frac_final, X_frac1_final, X_frac2_final, chiral_vec, R, filename)

    return H0_new, M_frac, X1_frac, natom_M, npair_X

def write_poscar(H1, elements, natom_M, npair_X, M_frac, X_frac1, X_frac2, chiral_vec, R, filename):
    with open(filename, 'w') as fid:
        fid.write(f"System: {chiral_vec[1]}x{chiral_vec[0]}-{elements[0]}{elements[1]}2-nanotube Diameter: {2*R:.6f} Angstrom\n")
        fid.write(f"{1.0:.6f}\n")
        for i in range(3):
            fid.write(f"{H1[i, 0]:12.6f} {H1[i, 1]:12.6f} {H1[i, 2]:12.6f}\n")
        fid.write(f"   {elements[0]}   {elements[1]}\n")
        fid.write(f"   {natom_M}   {2 * npair_X}\n")
        fid.write("Direct\n")
        for i in range(natom_M):
            fid.write(f"{M_frac[i, 0]:10.6f} {M_frac[i, 1]:10.6f} {M_frac[i, 2]:10.6f}\n")
        for i in range(npair_X):
            fid.write(f"{X_frac1[i, 0]:10.6f} {X_frac1[i, 1]:10.6f} {X_frac1[i, 2]:10.6f}\n")
        for i in range(npair_X):
            fid.write(f"{X_frac2[i, 0]:10.6f} {X_frac2[i, 1]:10.6f} {X_frac2[i, 2]:10.6f}\n")

    print(f"Nanotube POSCAR written to {filename}")

def read_chiral_indices(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # Skip the header
        chiral_indices = [tuple(map(int, line.split())) for line in lines]
    return chiral_indices

if __name__ == "__main__":
    poscar_file = "POSCAR_MoS2"
    chiral_indices = read_chiral_indices('chiral_index.txt')

    vacuum_layer = 15.0  # Adjust as needed
    Lz_unrolled = 20.0  # Adjust as needed

    for n, m in chiral_indices:
        fsave_name = f"MoS2_{n}_{m}"

        try:
            H0_new, M_frac, X1_frac, natom_M, npair_X = generate_nanotube_from_poscar(
                poscar_file, (n, m), vacuum_layer, fsave_name
            )
            print(f"Nanotube POSCAR generated for chiral vector ({n}, {m})")
        except Exception as e:
            print(f"Error generating POSCAR for chiral vector ({n}, {m}): {e}")

