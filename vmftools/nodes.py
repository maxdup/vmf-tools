from vmftools.property_values import *
from vmftools.property_parsers import *


class Node:
    FALLBACK = 'string'
    SCHEMA = {
        'id': 'integer',
        'classname': 'basnode'
    }
    # abstract class for vmf nodes

    def __init__(self, class_name):
        self._class_name = class_name
        self._properties = {}
        self._child_nodes = []
        self.depth = 0

    def __repr__(self):
        text = ('\t' * self.depth) + self._class_name + '\n'
        text += ('\t' * self.depth) + '{\n'

        for k, v in self._properties.items():
            text += ('\t' * (self.depth + 1))
            text += '"' + k + '" "' + repr_property_value(v) + '"\n'

        for n in self._child_nodes:
            n.depth = self.depth + 1
            text += repr(n)

        text += ('\t' * self.depth) + '}\n'
        return text

    def add_property(self, name, value):
        self._properties[name] = value

    def add_child(self, node):
        self._child_nodes.append(node)


# Node classes for vmf root
class versioninfo(Node):
    SCHEMA = {
        'id': 'integer',
        'prefab': 'bool',
        'editorversion': 'integer',
        'editorbuild': 'integer',
        'mapversion': 'integer',
        'formatversion': 'integer'
    }

    def __init__(self):
        Node.__init__(self, 'versioninfo')


class visgroups(Node):
    SCHEMA = {
        'id': 'integer',
        'visgroupid': 'integer',
        'color': 'color255'
    }

    def __init__(self):
        Node.__init__(self, 'visgroups')
        self._visgroups = []

    def add_child(self, node):
        if isinstance(node, visgroup):
            self._visgroups.append(node)
        Node.add_child(self, node)


class visgroup(Node):
    SCHEMA = {
        'name': 'string',
        'visgroupid': 'integer',
        'color': 'color255'
    }

    def __init__(self):
        Node.__init__(self, 'visgroup')
        self._visgroups = []

    def add_child(self, node):
        if isinstance(node, visgroup):
            self._visgroups.append(node)
        Node.add_child(self, node)


class viewsettings(Node):
    SCHEMA = {
        'id': 'integer',
        'bSnapToGrid': 'bool',
        'bShowGrid': 'bool',
        'bShowLogicalGrid': 'bool',
        'bShow3DGrid': 'bool',
        'nGridSpacing': 'integer'
    }

    def __init__(self):
        Node.__init__(self, 'viewsettings')


class world(Node):
    SCHEMA = {
        'id': 'integer',
        'mapversion': 'integer',
        'classname': 'string',
        'maxpropscreenwidth': 'integer',
        'detailmaterial': 'string',
        'detailvbsp': 'string',
        'skyname': 'string',
        'comment': 'string',
    }

    def __init__(self):
        Node.__init__(self, 'world')
        self._solids = []
        self._hiddens = []
        self._groups = []

    def add_child(self, node):
        if isinstance(node, solid):
            self._solids.append(node)
        elif isinstance(node, hidden):
            self._hiddens.append(node)
        elif isinstance(node, group):
            self._groups.append(node)

        Node.add_child(self, node)


class entity(Node):
    SCHEMA = {
        'id': 'integer',
        'classname': 'string',
        'origin': 'origin',
        'angles': 'angle',
    }

    def __init__(self, schema=None):
        Node.__init__(self, 'entity')
        self._connections = []
        self._solids = []
        self._hiddens = []
        self._groups = []
        self._editor = editor()

    def add_child(self, node):
        if isinstance(node, solid):
            self._solids.append(node)
        elif isinstance(node, connections):
            self._connections.append(node)
        elif isinstance(node, hidden):
            self._solids.append(node)
        elif isinstance(node, editor):
            self._editor = (node)

        Node.add_child(self, node)

    def mirror_x(self, x=0):
        solids = list(self._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                solids.extend(list(hidden._solids))

        for solid in solids:
            for side in solid._sides:
                side.mirror_x(x)

        for prop in self._properties:
            if isinstance(prop, origin):
                prop.mirror_y(y)
            if isinstance(prop, angle):
                prop.mirror_y(y)

    def mirror_y(self, y=0):
        solids = list(self._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                solids.eytend(list(hidden._solids))

        for solid in solids:
            for side in solid._sides:
                side.mirror_y(y)

        for prop in self._properties:
            if isinstance(prop, origin):
                prop.mirror_y(y)
            if isinstance(prop, angle):
                prop.mirror_y(y)

    def mirror_z(self, z=0):
        solids = list(self._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                solids.eztend(list(hidden._solids))

        for solid in solids:
            for side in solid._sides:
                side.mirror_z(z)

        for prop in self._properties:
            if isinstance(prop, origin):
                prop.mirror_y(y)
            if isinstance(prop, angle):
                prop.mirror_y(y)


class connections(Node):
    SCHEMA = {
        'id': 'integer'
    }

    def __init__(self):
        self.connections = []
        Node.__init__(self, 'connections')

    def add_property(self, property_name, value):
        self.connections.append((property_name, value))


class cordons(Node):
    SCHEMA = {
        'active': 'bool'
    }

    def __init__(self):
        Node.__init__(self, 'cordons')


class cordon(Node):
    SCHEMA = {
        'active': 'bool',
        'mins': 'vertex(',
        'maxs': 'vertex(',
    }

    def __init__(self):
        Node.__init__(self, 'cordon')
        self.box = None


class box(Node):
    SCHEMA = {
        'active': 'bool',
        'mins': 'vertex(',
        'maxs': 'vertex(',
    }

    def __init__(self):
        Node.__init__(self, 'cordon')


class cameras(Node):
    SCHEMA = {
        'activecamera': 'integer',
    }

    def __init__(self):
        Node.__init__(self, 'cameras')
        self._cameras = []


class camera(Node):
    SCHEMA = {
        'position': 'vertex[',
        'look': 'vertex[',
    }

    def __init__(self):
        Node.__init__(self, 'camera')


# node classes for World
class solid(Node):
    SCHEMA = {
        'id': 'integer'
    }

    def __init__(self):
        self._sides = []
        self._editor = editor()
        Node.__init__(self, 'solid')

    def add_child(self, node):
        if isinstance(node, side):
            self._sides.append(node)
        elif isinstance(node, editor):
            self.editor = node

        Node.add_child(self, node)

    def mirror_x(self, x=0):
        for side in self._sides:
            side.mirror_x(x)

    def mirror_y(self, y=0):
        for side in self._sides:
            side.mirror_y(y)

    def mirror_z(self, z=0):
        for side in self._sides:
            side.mirror_z(z)


class hidden(Node):
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'hidden')
        self._solids = []
        self._entities = []

    def add_child(self, node):
        if isinstance(node, solid):
            self._solids.append(node)
        elif isinstance(node, entity):
            self._entities.append(node)

        Node.add_child(self, node)


class group(Node):
    SCHEMA = {
        'id': 'integer'
    }

    def __init__(self):
        self._editor = editor()
        Node.__init__(self, 'group')


# child node class for solids
class side(Node):
    SCHEMA = {
        'id': 'integer',
        'plane': 'plane',
        'material': 'string',
        'uaxis': 'uvaxis',
        'vaxis': 'uvaxis',
        'lightmapscale': 'integer',
        'smoothing_groups': 'integer',
        'rotation': 'float',
    }

    def __init__(self):
        Node.__init__(self, 'side')
        self._dispinfo = None

    def add_child(self, node):
        if isinstance(node, dispinfo):
            self._dispinfo = node

        Node.add_child(self, node)

    def mirror_x(self, x=0):
        if 'plane' in self._properties:
            self._properties['plane'].mirror_x(x)

    def mirror_y(self, y=0):
        if 'plane' in self._properties:
            self._properties['plane'].mirror_y(y)

    def mirror_z(self, z=0):
        if 'plane' in self._properties:
            self._properties['plane'].mirror_z(z)


class editor(Node):
    SCHEMA = {
        'color': 'color255',
        'logicalpos': '2dvector',
        'visgroupid': 'integer',
        'groupid': 'integer',
        'visgroupshown': 'bool',
        'visgroupautoshown': 'bool'
    }

    def __init__(self):
        Node.__init__(self, 'editor')


# child Node class for sides
class dispinfo(Node):
    SCHEMA = {
        'power': 'integer',
        'startposition': 'vertex[',
        'flags': 'integer',
        'elevation': 'float',
        'subdiv': 'bool',
    }

    def __init__(self):
        Node.__init__(self, 'dispinfo')
        self._normals = None
        self._distances = None
        self._offsets = None
        self._offset_normals = None
        self._alphas = None
        self._triangle_tags = None
        self._allowed_verts = None

    def add_child(self, node):
        if isinstance(node, offsets):
            self._offsets = node
        elif isinstance(node, distances):
            self._distances = node
        elif isinstance(node, normals):
            self._normals = node
        elif isinstance(node, offset_normals):
            self._offset_normals = node
        elif isinstance(node, alphas):
            self._alphas = node
        elif isinstance(node, triangle_tags):
            self._triangle_tags = node
        elif isinstance(node, allowed_verts):
            self._allowed_verts = node

        Node.add_child(self, node)


# child Node classes for dispinfo


class disp_row_node(Node):
    SCHEMA = {}
    FALLBACK = 'vertex_row'

    def __repr__(self):
        # sort properties, print them
        text = ('\t' * self.depth) + self._class_name + '\n'
        text += ('\t' * self.depth) + '{\n'
        for k, v in self._properties.items():
            text += ('\t' * (self.depth + 1))
            text += '"' + str(k) + '" "'
            text += repr(v)
            text += '"\n'
        text += ('\t' * self.depth) + '}\n'
        return text


class normals(disp_row_node):
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'normals')


class offsets(disp_row_node):
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'offsets')


class offset_normals(disp_row_node):
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'offset_normals')


class distances(disp_row_node):
    FALLBACK = 'decimal_row'
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'distances')


class alphas(disp_row_node):
    FALLBACK = 'alpha_row'
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'alphas')


class triangle_tags(disp_row_node):
    FALLBACK = 'tritag_row'
    SCHEMA = {}

    def __init__(self):
        Node.__init__(self, 'triangle_tags')


class allowed_verts(Node):
    SCHEMA = {'10': 'allowed_row'}

    def __init__(self):
        Node.__init__(self, 'allowed_verts')
