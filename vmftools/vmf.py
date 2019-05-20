from vmftools.nodes import *


class VMF():

    def __init__(self):

        self._versioninfo = None
        self._visgroups = None
        self._viewsettings = None
        self._world = None
        self._entities = []
        self._hiddens = []
        self._cameras = None
        # some versions of hammer store a single cordon at the root
        self._cordon = None
        # some versions of hammer store multiple cordons
        self._cordons = None

        self.unknown_childs = []

        def add_child(self, node):
            if isinstance(node, versioninfo):
                self._versioninfo = node
            elif isinstance(node, visgroups):
                self._visgroups = node
            elif isinstance(node, viewsettings):
                self._viewsettings = node
            elif isinstance(node, world):
                self._world = node
            elif isinstance(node, entity):
                self._entities.append(node)
            elif isinstance(node, cameras):
                self._cameras = node
            elif isinstance(node, cordon):
                self._cordon = node
            elif isinstance(node, hidden):
                self._hiddens.append(node)
            elif isinstance(node, cordons):
                self._cordons = cordons
            elif isinstance(node, cordon):
                if self.cordons:
                    self.cordons.append(node)
                else:
                    self._cordon = cordon
            else:
                self.unknown_childs.append(node)
