class Node:
    # abstract class for vmf nodes
    def __init__(self, class_name):
        self.class_name = class_name
        self._properties = {}
        self.child_nodes = []

    def set_property(self, property_name, value):
        self._properties[property_name] = value

    def add_child(self, node):
        self.child_nodes.append(node)


# Node classes for vmf root
class versioninfo(Node):
    def __init__(self):
        Node.__init__(self, 'versioninfo')


class visgroups(Node):
    def __init__(self):
        Node.__init__(self, 'visgroups')


class visgroup(Node):
    def __init__(self):
        Node.__init__(self, 'visgroup')


class viewsettings(Node):
    def __init__(self):
        Node.__init__(self, 'viewsettings')


class world(Node):
    def __init__(self):
        Node.__init__(self, 'world')
        self.solids = []
        self.hiddens = []
        self.groups = []


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


class camera(Node):
    def __init__(self):
        Node.__init__(self, 'camera')

# node classes for World


class solid(Node):
    def __init__(self):
        Node.__init__(self, 'solif')


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


class editor(Node):
    def __init__(self):
        Node.__init__(self, 'editor')


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