def mirror_vmf_x(vmf, x=0):

    for solid in vmf.all_solids:
        solid.mirror_x(x)

    for entity in vmf.all_entities:
        entity.mirror_x(x)


def mirror_vmf_y(vmf, y=0):

    for solid in vmf.all_solids:
        solid.mirror_y(y)

    for entity in vmf.all_entities:
        entity.mirror_y(y)


def mirror_vmf_z(vmf, z=0):

    for solid in vmf.all_solids:
        solid.mirror_z(z)

    for entity in vmf.all_entities:
        entity.mirror_z(z)
