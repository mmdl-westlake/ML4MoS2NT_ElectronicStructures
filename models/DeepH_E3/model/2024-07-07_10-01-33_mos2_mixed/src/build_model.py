from deephe3_1 import Net
net = Net(
    num_species=2,
    irreps_embed_node='64x0e',
    irreps_edge_init='64x0e',
    irreps_sh='1x0e+1x1o+1x2e+1x3o+1x4e+1x5o',
    irreps_mid_node='64x0e+32x1o+16x2e+8x3o+8x4e',
    irreps_post_node='64x0e+32x1o+16x2e+8x3o+8x4e+32x1e',
    irreps_out_node='1x0e',
    irreps_mid_edge='64x0e+32x1o+16x2e+8x3o+8x4e',
    irreps_post_edge='40x0o+50x0e+96x1o+106x1e+88x2o+104x2e+48x3o+64x3e+16x4o+24x4e+8x5e',
    irreps_out_edge='1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e',
    num_block=3,
    r_max=7.2,
    use_sc=True,
    no_parity=False,
    use_sbf=False,
    only_ij=False,
    if_sort_irreps=False
)
