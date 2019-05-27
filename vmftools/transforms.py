def mirror_vmf_x(vmf, x=0):
    for solid in vmf.all_solids:
        solid.mirror_x(x)


def mirror_vmf_y(vmf, y=0):
    for solid in vmf.all_solids:
        solid.mirror_y(y)


def mirror_vmf_z(vmf, z=0):
    for solid in vmf.all_solids:
        solid.mirror_z(z)
