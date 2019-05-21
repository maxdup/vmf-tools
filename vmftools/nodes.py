from vmftools.property_values import *


class Node:
    # abstract class for vmf nodes
    def __init__(self, class_name):
        self.class_name = class_name
        self._properties = {}
        self.child_nodes = []

    def set_property(self, property_name, value):
        if property_name == 'id':
            self._properties[property_name] = int(value)
        else:
            self._properties[property_name] = value

    def add_child(self, node):
        self.child_nodes.append(node)


# Node classes for vmf root
class versioninfo(Node):
    def __init__(self):
        Node.__init__(self, 'versioninfo')

    def set_property(self, property_name, value):
        int_properties = ['editorversion', 'editorbuild', 'mapversion',
                          'formatversion', 'prefab']
        if property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.set_property(self, property_name, value)


class visgroups(Node):
    def __init__(self):
        Node.__init__(self, 'visgroups')


class visgroup(Node):
    def __init__(self):
        Node.__init__(self, 'visgroup')


class viewsettings(Node):
    def __init__(self):
        Node.__init__(self, 'viewsettings')

    def set_property(self, property_name, value):
        int_properties = ['bSnapToGrid', 'bShowGrid', 'bShowLogicalGrid',
                          'nGridSpacing', 'bShow3DGrid']
        if property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.set_property(self, property_name, value)


class world(Node):
    def __init__(self):
        Node.__init__(self, 'world')
        self.solids = []
        self.hiddens = []
        self.groups = []

    def set_property(self, property_name, value):
        int_properties = ['mapversion', 'maxpropscreenwidth']
        if property_name in int_properties:
            self._properties[property_name] = int(value)
        else:
            Node.set_property(self, property_name, value)


class entity(Node):
    def __init__(self):
        Node.__init__(self, 'entity')
        self.connections = []
        self.solids = []
        self.hiddens = []
        self.editor = None


class connections(Node):
    def __init__(self):
        Node.__init__(self, 'connections')


class cordons(Node):
    def __init__(self):
        Node.__init__(self, 'cordons')


class cordon(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')
        self.box = None


class box(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')


class cameras(Node):

    def __init__(self):
        Node.__init__(self, 'cameras')
        self.cameras = []

    def set_property(self, property_name, value):
        vertex
        if property_name == 'position':
            self._properties[property_name] = int(value)
        else:
            Node.set_property(self, property_name, value)


class camera(Node):
    def __init__(self):
        Node.__init__(self, 'camera')

    def set_property(self, property_name, value):
        vertex_properties = ['position', 'look']
        if property_name in vertex_properties:
            self._properties[property_name] = parse_vertex(value)
        else:
            Node.set_property(self, property_name, value)

# node classes for World


class solid(Node):
    def __init__(self):
        Node.__init__(self, 'solid')


class hidden(Node):
    def __init__(self):
        Node.__init__(self, 'hidden')


class group(Node):
    def __init__(self):
        Node.__init__(self, 'group')


# child node class for solids
class side(Node):
    def __init__(self):
        Node.__init__(self, 'side')

    def set_property(self, property_name, value):
        if property_name == 'plane':
            self._properties[property_name] = parse_plane(value)
        elif property_name == 'uaxis' or property_name == 'vaxis':
            self._properties[property_name] = parse_uvaxis(value)
        elif property_name == 'lightmapscale' or \
                property_name == 'smoothing_groups':
            self._properties[property_name] = int(value)
        elif property_name == 'rotation':
            self._properties[property_name] = parse_decimal(value)
        else:
            Node.set_property(self, property_name, value)


class editor(Node):
    def __init__(self):
        Node.__init__(self, 'editor')

    def set_property(self, property_name, value):
        if property_name == 'color ':
            self._properties[property_name] = parse_rgb(value)
        elif property_name == 'logicalpos':
            self._properties[property_name] = parse_twodvector(value)
        elif property_name in ['visgroupid', 'groupid']:
            self._properties[property_name] = int(value)
        elif property_name in ['visgroupshown', 'visgroupautoshown']:
            self._properties[property_name] = parse_boolean(value)
        else:
            Node.set_property(self, property_name, value)


# child Node class for sides
class dispinfo(Node):
    def __init__(self):
        Node.__init__(self, 'dispinfo')


# child Node classes for dispinfo
class normals(Node):
    def __init__(self):
        Node.__init__(self, 'normals')


class distances(Node):
    def __init__(self):
        Node.__init__(self, 'distances')


class offsets(Node):
    def __init__(self):
        Node.__init__(self, 'offsets')


class offset_normals(Node):
    def __init__(self):
        Node.__init__(self, 'offset_normals')


class alphas(Node):
    def __init__(self):
        Node.__init__(self, 'alphas')


class triangle_tags(Node):
    def __init__(self):
        Node.__init__(self, 'triangle_tags')


class allowed_verts(Node):
    def __init__(self):
        Node.__init__(self, 'allowed_verts')
