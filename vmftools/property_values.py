from decimal import Decimal
import re


class vector():  # an abstract vector xyz
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __repr__(self):
        s = repr_property_value(self._x) + ' ' + \
            repr_property_value(self._y) + ' ' + \
            repr_property_value(self._z)
        return s


class angle(vector):
    def __init__(self, x, y, z):
        vector.__init__(self, x, y, z)

    def mirror_x(self, x=0):
        pass

    def mirror_y(self, y=0):
        pass

    def mirror_z(self, z=0):
        pass


class origin(vector):
    def __init__(self, x, y, z):
        vector.__init__(self, x, y, z)

    def mirror_x(self, x=0):
        self._x = x - (self._x - x)

    def mirror_y(self, y=0):
        self._y = y - (self._y - y)

    def mirror_z(self, z=0):
        self._z = z - (self._z - z)


class vertex(origin):
    def __init__(self, x, y, z, wrapper=''):
        vector.__init__(self, x, y, z)
        self.wrapper = wrapper

    def __repr__(self):
        # Represented as: (0 0 0) or [0 0 0]
        s = origin.__repr__(self)
        if (self.wrapper == '('):
            s = '(' + s + ')'
        elif (self.wrapper == '['):
            s = '[' + s + ']'
        return s


class plane():
    def __init__(self, v1, v2, v3):
        self._v1 = v1
        self._v2 = v2
        self._v3 = v3

    def __repr__(self):
        # Represented as: (0 0 0) (0 0 0) (0 0 0)
        s = repr(self._v1) + ' ' + \
            repr(self._v2) + ' ' + \
            repr(self._v3)
        return s

    def mirror_reorder(self):
        v3 = self._v3
        self._v3 = self._v1
        self._v1 = v3

    def mirror_x(self, x=0):
        self._v1.mirror_x(x)
        self._v2.mirror_x(x)
        self._v3.mirror_x(x)
        self.mirror_reorder()

    def mirror_y(self, y=0):
        self._v1.mirror_y(y)
        self._v2.mirror_y(y)
        self._v3.mirror_y(y)
        self.mirror_reorder()

    def mirror_z(self, z=0):
        self._v1.mirror_z(z)
        self._v2.mirror_z(z)
        self._v3.mirror_z(z)
        self.mirror_reorder()


class color255():
    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    def __repr__(self):
        # Represented as: 255 255 255
        return repr(self._r) + ' ' + \
            repr(self._g) + ' ' + \
            repr(self._b)


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
        return row.strip(' ')


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
