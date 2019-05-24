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
        s = repr_property_value(self._x) + ' ' + \
            repr_property_value(self._y) + ' ' + \
            repr_property_value(self._z)
        if (self.type == 'plane'):
            s = '(' + s + ')'
        else:
            s = '[' + s + ']'
        return s


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
            repr_property_value(self._x) + ' ' + \
            repr_property_value(self._y) + ' ' + \
            repr_property_value(self._z) + ' ' + \
            repr_property_value(self._t) + '] ' + \
            repr_property_value(self._scale)


class twodvector():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        s = '[' + \
            repr_property_value(self._x) + ' ' + \
            repr_property_value(self._y) + ']'
        return s


class value_row():
    def __init__(self, vals):
        self._row = vals

    def __repr__(self):
        # Represented as: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        row = ''
        for r in self._row:
            row += repr_property_value(r).strip('[').strip(']') + ' '
        return row.strip()


def repr_property_value(val):
    if isinstance(val, str):
        return val
    elif isinstance(val, Decimal):
        return '{:.6g}'.format(val)
    elif isinstance(val, bool):
        return '1' if val else '0'
    elif isinstance(val, int):
        return str(val)
    else:
        return repr(val)
