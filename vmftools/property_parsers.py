from vmftools.property_values import *


def parse_properties(raw_properties, schema, fallback=None):
    properties = {}
    for k, v in raw_properties.items():
        type = ''
        if k in schema:
            type = schema[k]
        else:
            type = fallback

        if type == 'bool':
            properties[k] = parse_bool(v)
        elif type == 'float':
            properties[k] = parse_float(v)
        elif type == 'integer' or \
                type == 'choices' or \
                type == 'flags':
            properties[k] = parse_int(v)
        elif type == 'plane':
            properties[k] = parse_plane(v)
        elif type == 'uvaxis':
            properties[k] = parse_uvaxis(v)
        elif type == 'color255':
            properties[k] = parse_color255(v)
        elif type == 'origin':
            properties[k] = parse_origin(v)
        elif type == 'angle':
            properties[k] = parse_angle(v)
        elif type == '2dvector':
            properties[k] = parse_twodvector(v)
        elif type == 'vertex':
            properties[k] = parse_vertex(v)
        elif type == 'vertex[':
            properties[k] = parse_vertex(v, '[')
        elif type == 'vertex(':
            properties[k] = parse_vertex(v, '(')
        elif type == 'vertex_row':
            properties[k] = parse_vertex_row(v)
        elif type == 'alpha_row':
            properties[k] = parse_alpha_row(v)
        elif type == 'tritag_row':
            properties[k] = parse_tritag_row(v)
        elif type == 'decimal_row':
            properties[k] = parse_decimal_row(v)
        elif type == 'allowed_row':
            properties[k] = parse_allowed_row(v)
        elif type == 'string' or \
                type == 'material':
            properties[k] = v
        else:
            properties[k] = v

    return properties


def parse_bool(value):
    return bool(int(value))


def parse_float(value):
    return Decimal(value)


def parse_int(value):
    # Hammer can and will put floating values
    # into properties tagged as integer
    try:
        return int(value)
    except:
        try:
            return decimal(value)
        except:
            return value


def parse_string(value):
    return value


def parse_void(value):
    return value


def parse_angle(string_repr):
    vals = string_repr.split(' ')
    a = angle(Decimal(vals[0]), Decimal(vals[1]),
              Decimal(vals[2]))
    return a


def parse_origin(string_repr):
    vals = string_repr.split(' ')
    o = origin(Decimal(vals[0]), Decimal(vals[1]),
               Decimal(vals[2]))
    return o


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


def parse_color255(string_repr):
    vals = string_repr.split(' ')
    return color255(min(255, max(-1, int(vals[0]))),
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
