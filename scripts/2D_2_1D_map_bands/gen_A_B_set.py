###Created by Ju Huang: huangju33@gmail.com
###generate all related parameters of nanotubes with chiral index of(n,m), e.g. MoS2
import numpy as np
from math import gcd
import csv

def calculate_xy_values(n, m):
    
    a = 3.184  # Mo-S distance
    
    a1 = np.array([np.sqrt(3)/2 * a, 1/2 * a])
    a2 = np.array([np.sqrt(3)/2 * a, -1/2 * a])

    Ch = n * a1 + m * a2

    dR = gcd(2 * n + m, 2 * m + n)

    t1 = (2 * m + n) / dR
    t2 = -(2 * n + m) / dR
    T_vec = t1 * a1 + t2 * a2

    N = 2 * (n**2 + m**2 + n * m) / dR

    b1 = np.array([2 * np.pi/np.sqrt(3)/a, 2 * np.pi/a])
    b2 = np.array([2 * np.pi/np.sqrt(3)/a, -2 * np.pi/a])

    b1_b2 = np.column_stack((b1, b2))

    K1 = (-t2 * b1 + t1 * b2) / N
    K2 = (m * b1 - n * b2) / N

    abs_K2 = np.linalg.norm(K2)

    T = np.sqrt(3) * a * np.sqrt(n**2 + m**2 + n * m) / dR

    xy_values = []

    for u in range(int(N)):
        A = (-np.pi/T) * (K2/abs_K2) + u * K1
        B = (np.pi/T) * (K2/abs_K2) + u * K1

        x_A, y_A = np.linalg.solve(b1_b2, A)
        x_B, y_B = np.linalg.solve(b1_b2, B)

        xy_values.append((n, m, u, N, x_A, y_A, x_B, y_B))

    return xy_values

n, m = 20, 0

xy_results = calculate_xy_values(n, m)

csv_file_name = "info_A_B_set.csv"

with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["n", "m", "u", "N", "x_A", "y_A", "x_B", "y_B"])

    for result in xy_results:
        writer.writerow(result)

print(f"Results saved to {csv_file_name}")
