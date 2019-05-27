from vmftools.property_values import *
from vmftools.property_parsers import *


class Node:
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

    def parse_property(self, property_name, value):
        if property_name == 'id':
            self._properties[property_name] = int(value)
        else:
            self._properties[property_name] = value

    def add_child(self, node):
        self._child_nodes.append(node)


# Node classes for vmf root
class versioninfo(Node):
    def __init__(self):
        Node.__init__(self, 'versioninfo')

    def parse_property(self, property_name, value):
        int_properties = ['editorversion', 'editorbuild', 'mapversion',
                          'formatversion']
        if property_name == 'prefab':
            self._properties[property_name] = bool(int(value))
        elif property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)


class visgroups(Node):
    def __init__(self):
        Node.__init__(self, 'visgroups')
        self._visgroups = []

    def parse_property(self, property_name, value):
        if property_name == 'visgroupid':
            self._properties[property_name] = int(value)
        elif property_name == 'color':
            self._properties[property_name] = parse_rgb(value)
        else:
            Node.parse_property(self, property_name, value)

    def add_child(self, node):
        if isinstance(node, visgroup):
            self._visgroups.append(node)
        Node.add_child(self, node)


class visgroup(Node):
    def __init__(self):
        Node.__init__(self, 'visgroup')
        self._visgroups = []

    def parse_property(self, property_name, value):
        if property_name == 'visgroupid':
            self._properties[property_name] = int(value)
        elif property_name == 'color':
            self._properties[property_name] = parse_rgb(value)
        else:
            Node.parse_property(self, property_name, value)

    def add_child(self, node):
        if isinstance(node, visgroup):
            self._visgroups.append(node)
        Node.add_child(self, node)


class viewsettings(Node):
    def __init__(self):
        Node.__init__(self, 'viewsettings')

    def parse_property(self, property_name, value):
        bool_properties = ['bSnapToGrid', 'bShowGrid',
                           'bShowLogicalGrid', 'bShow3DGrid']
        if property_name in bool_properties:
            self._properties[property_name] = bool(int(value))
        elif property_name == 'nGridSpacing':
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)


class world(Node):
    def __init__(self):
        Node.__init__(self, 'world')
        self._solids = []
        self._hiddens = []
        self._groups = []

    def parse_property(self, property_name, value):
        int_properties = ['mapversion', 'maxpropscreenwidth']
        if property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)

    def add_child(self, node):
        if isinstance(node, solid):
            self._solids.append(node)
        elif isinstance(node, hidden):
            self._hiddens.append(node)
        elif isinstance(node, group):
            self._groups.append(node)

        Node.add_child(self, node)


class entity(Node):

    def __init__(self):
        Node.__init__(self, 'entity')
        self._connections = []
        self._solids = []
        self._hiddens = []
        self._groups = []
        self._editor = editor()

    def parse_property(self, property_name, value):
        if property_name == 'origin':
            self._properties[property_name] = parse_vertex(value)
        elif property_name == 'spawnflags':
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)

    def add_child(self, node):
        if isinstance(node, solid):
            self._solids.append(node)
        if isinstance(node, hidden):
            self._solids.append(node)
        if isinstance(node, editor):
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

        if 'origin' in self._properties:
            self._properties['origin'].mirror_x(x)

    def mirror_y(self, y=0):
        solids = list(self._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                solids.eytend(list(hidden._solids))

        for solid in solids:
            for side in solid._sides:
                side.mirror_y(y)

        if 'origin' in self._properties:
            self._properties['origin'].mirror_y(y)

    def mirror_z(self, z=0):
        solids = list(self._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                solids.eztend(list(hidden._solids))

        for solid in solids:
            for side in solid._sides:
                side.mirror_z(z)

        if 'origin' in self._properties:
            self._properties['origin'].mirror_z(z)


class connections(Node):

    def __init__(self):
        self.connections = []
        Node.__init__(self, 'connections')

    def parse_property(self, property_name, value):
        self.connections.append((property_name, value))


class cordons(Node):
    def __init__(self):
        Node.__init__(self, 'cordons')

    def parse_property(self, property_name, value):
        if property_name == 'active':
            self._properties[property_name] = bool(int(value))
        else:
            Node.parse_property(self, property_name, value)


class cordon(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')
        self.box = None

    def parse_property(self, property_name, value):
        if property_name == 'active':
            self._properties[property_name] = bool(int(value))
        elif property_name == 'mins' or property_name == 'maxs':
            self._properties[property_name] = parse_vertex(value, '(')
        else:
            Node.parse_property(self, property_name, value)


class box(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')

    def parse_property(self, property_name, value):
        if property_name == 'active':
            self._properties[property_name] = bool(int(value))
        elif property_name == 'mins' or property_name == 'maxs':
            self._properties[property_name] = parse_vertex(value, '(')
        else:
            Node.parse_property(self, property_name, value)


class cameras(Node):

    def __init__(self):
        Node.__init__(self, 'cameras')
        self._cameras = []

    def parse_property(self, property_name, value):
        if property_name == 'activecamera':
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)


class camera(Node):
    def __init__(self):
        Node.__init__(self, 'camera')

    def parse_property(self, property_name, value):
        if property_name in ['position', 'look']:
            self._properties[property_name] = parse_vertex(value, '[')
        else:
            Node.parse_property(self, property_name, value)


# node classes for World
class solid(Node):
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
    def __init__(self):
        self._editor = editor()
        Node.__init__(self, 'group')


# child node class for solids
class side(Node):
    def __init__(self):
        Node.__init__(self, 'side')
        self._dispinfo = None

    def parse_property(self, property_name, value):
        if property_name == 'plane':
            self._properties[property_name] = parse_plane(value)
        elif property_name == 'uaxis' or property_name == 'vaxis':
            self._properties[property_name] = parse_uvaxis(value)
        elif property_name == 'lightmapscale' or \
                property_name == 'smoothing_groups':
            self._properties[property_name] = int(value)
        elif property_name == 'rotation':
            self._properties[property_name] = Decimal(value)
        else:
            Node.parse_property(self, property_name, value)

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
    def __init__(self):
        Node.__init__(self, 'editor')

    def parse_property(self, property_name, value):
        if property_name == 'color':
            self._properties[property_name] = parse_rgb(value)
        elif property_name == 'logicalpos':
            self._properties[property_name] = parse_twodvector(value)
        elif property_name in ['visgroupid', 'groupid']:
            self._properties[property_name] = int(value)
        elif property_name in ['visgroupshown', 'visgroupautoshown']:
            self._properties[property_name] = bool(int(value))
        else:
            Node.parse_property(self, property_name, value)


# child Node class for sides
class dispinfo(Node):
    def __init__(self):
        Node.__init__(self, 'dispinfo')
        self._normals = None
        self._distances = None
        self._offsets = None
        self._offset_normals = None
        self._alphas = None
        self._triangle_tags = None
        self._allowed_verts = None

    def parse_property(self, property_name, value):
        if property_name == 'power':
            self._properties[property_name] = min(2, max(4, int(value)))
        elif property_name == 'startposition':
            self._properties[property_name] = parse_vertex(value, '[')
        elif property_name == 'subdiv':
            self._properties[property_name] = bool(int(value))
        elif property_name == 'elevation':
            self._properties[property_name] = Decimal(value)
        else:
            Node.parse_property(self, property_name, value)

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

    def __init__(self):
        self._rows = []

    def __repr__(self):
        text = ('\t' * self.depth) + self._class_name + '\n'
        text += ('\t' * self.depth) + '{\n'
        for i in range(0, len(self._rows)):
            text += ('\t' * (self.depth + 1))
            text += '"' + 'row' + str(i) + '" "'
            text += repr(self._rows[i])
            text += '"\n'
        text += ('\t' * self.depth) + '}\n'
        return text

    def parse_property(self, row_string, value):
        rowId = int(''.join(re.findall(r'\d+', row_string)))
        if rowId >= len(self._rows):
            for i in range(len(self._rows), rowId+1):
                self._rows.append(None)
        row = self.parser(value)
        self._rows[rowId] = row


class normals(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'normals')
        self.parser = parse_vertex_row


class offsets(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'offsets')
        self.parser = parse_vertex_row


class offset_normals(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'offset_normals')
        self.parser = parse_vertex_row


class distances(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'distances')
        self.parser = parse_decimal_row


class alphas(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'alphas')
        self.parser = parse_alpha_row


class triangle_tags(disp_row_node):
    def __init__(self):
        disp_row_node.__init__(self)
        Node.__init__(self, 'triangle_tags')
        self.parser = parse_tritag_row


class allowed_verts(Node):
    # ints
    def __init__(self):
        self._allows = []
        Node.__init__(self, 'allowed_verts')

    def parse_property(self, property_name, value):
        if property_name == '10':
            self._properties[property_name] = parse_allowed_row(value)
