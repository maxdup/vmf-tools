import re
from decimal import Decimal


class vertex():
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __repr__(self, plane=False):
        # Represented as: (0 0 0) or [0 0 0]
        s = str(self._x) + ' ' + str(self._y) + ' ' + str(self._z)
        if (plane):
            s = '(' + s + ')'
        else:
            s = '[' + s + ']'
        return s


def parse_vertex(string_repr):
    vals = string_repr.strip().strip(
        '(').strip(')').strip('[').strip(']').split(' ')
    v = vertex(parse_decimal(vals[0]),
               parse_decimal(vals[1]),
               parse_decimal(vals[2]))
    return v


class vertex_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        row = ''
        for r in self._row:
            row += repr(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_vertex_row(string_repr):
    vals = string_repr.split(' ')
    vertices = []
    for i in range(0, int(len(vals)/3)):
        vertices.append(vertex(vals[i*3+0], vals[i*3+1], vals[i*3+2]))
    vr = vertex_row(vertices)
    return vr


class plane():
    def __init__(self, v1, v2, v3):
        self._v1 = v1
        self._v2 = v2
        self._v3 = v3

    def __repr__(self):
        # Represented as: (0 0 0) (0 0 0) (0 0 0)
        return repr(self._v1, True) + \
            ' ' + repr(self._v2) + \
            ' ' + repr(self._v3)


def parse_plane(string_repr):
    string_repr = string_repr.strip(' ').strip(')').strip('(')
    vals = string_repr.replace(') (', ')(').split(')(')
    p = plane(parse_vertex(vals[0]),
              parse_vertex(vals[1]),
              parse_vertex(vals[2]))
    return p


class rgb():
    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        # Represented as: 255 255 255
        return repr(self._r) + ' ' + repr(self._g) + ' ' + \
            repr(self._b) + ' '


def parse_rgb(string_repr):
    vals = string_repr.split(' ')
    return rgb(int(vals[0]), int(vals[1]), int(vals[2]))


class uvaxis():
    def __init__(self, x, y, z, t, scale):
        self._x = x
        self._y = y
        self._z = z
        self._t = t
        self._scale = scale

    def __repr__(self):
        # Represented as: [0 0 1 0] 0.25
        return '[' + \
            repr(self._x) + ' ' + repr(self._y) + ' ' + \
            repr(self._z) + ' ' + repr(self._t) + '] ' + repr(self._scale)


def parse_uvaxis(string_repr):
    vals = string_repr.split(']')
    scale = vals[-1]
    coords = vals[0].strip('[').split(' ')
    axis = uvaxis(parse_decimal(coords[0]), parse_decimal(coords[1]),
                  parse_decimal(coords[2]), parse_decimal(coords[3]),
                  parse_decimal(scale))
    return axis


class twodvector():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        s = '[' + repr(self._x) + ' ' + repr(self._y) + ']'
        return s


def parse_twodvector(string_repr):
    vals = string_repr.strip().strip('[').strip(']').strip().split(' ')
    v = twodvector(parse_decimal(vals[0]), parse_decimal(vals[1]))
    return v


class decimal():
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(self._value)


def parse_decimal(string_repr):
    d = decimal(Decimal(string_repr))
    return d


class boolean():
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return str(int(self._value))


def parse_boolean(string_repr):
    b = (string_repr == '1')
    return b
