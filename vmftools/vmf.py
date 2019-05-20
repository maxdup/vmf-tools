class VMF():

    def __init__(self):
        self.nodes = []

        self.world = None
        self.versioninfo = None
        self.cameras = None
        self.cordon = None
        self.viewsettings = None


class Node:

    def __init__(self):
        self.properties = {}
        self.child_nodes = []
        self.p_args = []


class versioninfo(Node):
    pass


class visgroups(Node):
    pass


class viewsettings(Node):
    pass


class world(Node):
    pass


class entity(Node):
    pass


class cordon(Node):
    pass


class cameras(Node):
    pass


class solid(Node):
    pass


class side(Node):
    pass


class dispinfo(Node):
    pass
