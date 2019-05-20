class VMF():

    def __init__(self):

        self.versioninfo = None
        self.visgroups = None
        self.viewsettings = None
        self.world = None
        self.entities = []
        self.cameras = None
        self.cordon = None

        self.unknown_nodes = []


class Node:
    # abstract class for vmf node
    def __init__(self, class_name):
        self.class_name = class_name
        self.properties = {}
        self.child_nodes = []


class versioninfo(Node):
    def __init__(self):
        Node.__init__(self, 'versioninfo')


class visgroups(Node):
    def __init__(self):
        Node.__init__(self, 'visgroups')


class viewsettings(Node):
    def __init__(self):
        Node.__init__(self, 'viewsettings')


class world(Node):
    def __init__(self):
        Node.__init__(self, 'world')


class entity(Node):
    def __init__(self):
        Node.__init__(self, 'entity')


class cordon(Node):
    def __init__(self):
        Node.__init__(self, 'cordon')


class cameras(Node):
    def __init__(self):
        Node.__init__(self, 'cameras')


class solid(Node):
    def __init__(self):
        Node.__init__(self, 'solif')


class side(Node):
    def __init__(self):
        Node.__init__(self, 'side')


class dispinfo(Node):
    def __init__(self):
        Node.__init__(self, 'dispinfo')


class editor(Node):
    def __init__(self):
        Node.__init__(self, 'editor')


class group(Node):
    def __init__(self):
        Node.__init__(self, 'group')


# dispinfo child nodes
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


class hidden(Node):
    def __init__(self):
        Node.__init__(self, 'hidden')
