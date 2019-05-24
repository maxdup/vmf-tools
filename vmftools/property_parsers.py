from vmftools.property_values import *


def parse_vertex(string_repr, wrapper=''):
    vals = string_repr.strip().strip(
        '(').strip(')').strip('[').strip(']').split(' ')
    v = vertex(Decimal(vals[0]), Decimal(vals[1]),
               Decimal(vals[2]), wrapper)
    v.type = 'plane' if plane else 'entity'
    return v


def parse_plane(string_repr):
    string_repr = string_repr.strip(' ').strip(')').strip('(')
    vals = string_repr.replace(') (', ')(').split(')(')
    p = plane(parse_vertex(vals[0], '('),
              parse_vertex(vals[1], '('),
              parse_vertex(vals[2], '('))
    return p


def parse_rgb(string_repr):
    vals = string_repr.split(' ')
    return rgb(min(255, max(-1, int(vals[0]))),
               min(255, max(-1, int(vals[1]))),
               min(255, max(-1, int(vals[2]))))


def parse_uvaxis(string_repr):
    vals = string_repr.split(']')
    scale = vals[-1]
    coords = vals[0].strip('[').split(' ')
    axis = uvaxis(Decimal(coords[0]), Decimal(coords[1]),
                  Decimal(coords[2]), Decimal(coords[3]),
                  Decimal(scale))
    return axis


def parse_twodvector(string_repr):
    vals = string_repr.strip().strip('[').strip(']').strip().split(' ')
    v = twodvector(Decimal(vals[0]), Decimal(vals[1]))
    return v


def parse_vertex_row(string_repr):
    vals = string_repr.split(' ')
    vertices = []
    for i in range(0, int(len(vals)/3)):
        v = vertex(Decimal(vals[i*3+0]),
                   Decimal(vals[i*3+1]),
                   Decimal(vals[i*3+2]))
        vertices.append(v)
    vr = value_row(vertices)
    return vr


def parse_decimal_row(string_repr):
    vals = string_repr.split(' ')
    decimals = []
    for i in range(0, len(vals)):
        decimals.append(Decimal(vals[i]))
    dr = value_row(decimals)
    return dr


def parse_alpha_row(string_repr):
    vals = string_repr.split(' ')
    alphas = []
    for i in range(0, len(vals)):
        alphas.append(min(255, max(-1, Decimal(vals[i]))))
    ar = value_row(alphas)
    return ar


def parse_tritag_row(string_repr):
    vals = string_repr.split(' ')
    tags = []
    for i in range(0, len(vals)):
        val = int(vals[i])
        if val != 0 and val != 1 and val != 9:
            val = 0
        tags.append(val)
    tr = value_row(tags)
    return tr


def parse_allowed_row(string_repr):
    vals = string_repr.split(' ')
    allows = []
    for i in range(0, len(vals)):
        allows.append(int(vals[i]))
    ar = value_row(allows)
    return ar
