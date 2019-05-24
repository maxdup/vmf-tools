from decimal import Decimal
import re


class vertex():
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self.type = 'entity'  # or 'plane'

    def __repr__(self):
        # Represented as: (0 0 0) or [0 0 0]
        s = str(self._x) + ' ' + str(self._y) + ' ' + str(self._z)
        if (self.type == 'plane'):
            s = '(' + s + ')'
        else:
            s = '[' + s + ']'
        return s


def parse_vertex(string_repr, plane=False):
    vals = string_repr.strip().strip(
        '(').strip(')').strip('[').strip(']').split(' ')
    v = vertex(Decimal(vals[0]),
               Decimal(vals[1]),
               Decimal(vals[2]))
    v.type = 'plane' if plane else 'entity'
    return v


class vertex_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        row = ''
        for r in self._row:
            row += repr(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_vertex_row(string_repr):
    vals = string_repr.split(' ')
    vertices = []
    for i in range(0, int(len(vals)/3)):
        v = vertex(Decimal(vals[i*3+0]),
                   Decimal(vals[i*3+1]),
                   Decimal(vals[i*3+2]))
        vertices.append(v)
    vr = vertex_row(vertices)
    return vr


class plane():
    def __init__(self, v1, v2, v3):
        self._v1 = v1
        self._v1.type = "plane"
        self._v2 = v2
        self._v2.type = "plane"
        self._v3 = v3
        self._v3.type = "plane"

    def __repr__(self):
        # Represented as: (0 0 0) (0 0 0) (0 0 0)
        s = repr(self._v1) + ' ' + \
            repr(self._v2) + ' ' + \
            repr(self._v3)
        return s


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
        return repr(self._r) + 'x ' + \
            repr(self._g) + ' ' + \
            repr(self._b) + ' '


def parse_rgb(string_repr):
    vals = string_repr.split(' ')
    return rgb(min(255, max(-1, int(vals[0]))),
               min(255, max(-1, int(vals[1]))),
               min(255, max(-1, int(vals[2]))))


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
            str(self._x) + ' ' + str(self._y) + ' ' + \
            str(self._z) + ' ' + str(self._t) + '] ' + str(self._scale)


def parse_uvaxis(string_repr):
    vals = string_repr.split(']')
    scale = vals[-1]
    coords = vals[0].strip('[').split(' ')
    axis = uvaxis(Decimal(coords[0]), Decimal(coords[1]),
                  Decimal(coords[2]), Decimal(coords[3]),
                  Decimal(scale))
    return axis


class twodvector():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        s = '[' + str(self._x) + ' ' + str(self._y) + ']'
        return s


def parse_twodvector(string_repr):
    vals = string_repr.strip().strip('[').strip(']').strip().split(' ')
    v = twodvector(Decimal(vals[0]), Decimal(vals[1]))
    return v


class decimal_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        row = ''
        for r in self._row:
            row += str(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_decimal_row(string_repr):
    vals = string_repr.split(' ')
    decimals = []
    for i in range(0, len(vals)):
        decimals.append(Decimal(vals[i]))
    dr = decimal_row(decimals)
    return dr


class alpha_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: 0 0 0 0 0
        row = ''
        for r in self._row:
            row += str(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_alpha_row(string_repr):
    vals = string_repr.split(' ')
    alphas = []
    for i in range(0, len(vals)):
        alphas.append(min(255, max(-1, Decimal(vals[i]))))
    ar = alpha_row(alphas)
    return ar


class tritag_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: 9 9 9 9 9 9 9 9
        row = ''
        for r in self._row:
            row += repr(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_tritag_row(string_repr):
    vals = string_repr.split(' ')
    tags = []
    for i in range(0, len(vals)):
        val = int(vals[i])
        if val != 0 and val != 1 and val != 9:
            val = 0
        tags.append(val)
    tr = tritag_row(tags)
    return tr


class allows_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
        row = ''
        for r in self._row:
            row += repr(r).strip('[').strip(']') + ' '
        return row.strip()


def parse_allowed_row(string_repr):
    vals = string_repr.split(' ')
    allows = []
    for i in range(0, len(vals)):
        allows.append(int(vals[i]))
    ar = allows_row(allows)
    return ar
