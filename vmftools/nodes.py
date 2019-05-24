from vmftools.property_values import *


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

    def parse_property(self, property_name, value):
        if property_name == 'visgroupid':
            self._properties[property_name] = int(value)
        elif property_name == 'color':
            self._properties[property_name] = parse_rgb(value)
        else:
            Node.parse_property(self, property_name, value)


class visgroup(Node):
    def __init__(self):
        Node.__init__(self, 'visgroup')

    def parse_property(self, property_name, value):
        if property_name == 'visgroupid':
            self._properties[property_name] = int(value)
        elif property_name == 'color':
            self._properties[property_name] = parse_rgb(value)
        else:
            Node.parse_property(self, property_name, value)


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
        self.solids = []
        self.hiddens = []
        self.groups = []

    def parse_property(self, property_name, value):
        int_properties = ['mapversion', 'maxpropscreenwidth']
        if property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)


class entity(Node):

    def __init__(self):
        Node.__init__(self, 'entity')
        self._connections = []
        self._solids = []
        self._hiddens = []
        self._editor = editor()

    def parse_property(self, property_name, value):
        if property_name == 'origin':
            self._properties[property_name] = parse_vertex(value)
        elif property_name == 'spawnflags':
            self._properties[property_name] = int(value)
        else:
            Node.parse_property(self, property_name, value)


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
            self._properties[property_name] = parse_vertex(value)
        else:
            Node.parse_property(self, property_name, value)


class box(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')

    def parse_property(self, property_name, value):
        if property_name == 'active':
            self._properties[property_name] = bool(int(value))
        elif property_name == 'mins' or property_name == 'maxs':
            self._properties[property_name] = parse_vertex(value)
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
            self._properties[property_name] = parse_vertex(value)
        else:
            Node.parse_property(self, property_name, value)

# node classes for World


class solid(Node):
    def __init__(self):
        self._sides = []
        self._editor = editor()
        Node.__init__(self, 'solid')


class hidden(Node):
    def __init__(self):
        Node.__init__(self, 'hidden')
        self._solid = None
        self._entity = None


class group(Node):
    def __init__(self):
        self._editor = editor()
        Node.__init__(self, 'group')


# child node class for solids
class side(Node):
    def __init__(self):
        Node.__init__(self, 'side')

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
            self._properties[property_name] = parse_vertex(value)
        elif property_name == 'subdiv':
            self._properties[property_name] = bool(int(value))
        elif property_name == 'elevation':
            self._properties[property_name] = Decimal(value)
        else:
            Node.parse_property(self, property_name, value)

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
