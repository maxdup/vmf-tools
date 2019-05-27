def mirror_vmf_x(vmf, x=0):
    for solid in vmf.all_solids:
        solid.mirror_x(x)
