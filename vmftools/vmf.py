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

        self._child_nodes = []

    def __repr__(self):
        text = ''
        if self._versioninfo:
            text += repr(self._versioninfo)
        if self._visgroups:
            text += repr(self._visgroups)
        if self._viewsettings:
            text += repr(self._viewsettings)
        if self._world:
            text += repr(self._world)
        if self._entities:
            for ent in self._entities:
                text += repr(ent)
        if self._hiddens:
            for hid in self._hiddens:
                text += repr(hid)
        if self._cameras:
            text += repr(self._cameras)
        if self._cordon:
            text += repr(self._cordon)
        if self._cordons:
            text += repr(self._cordons)

        return text

    @property
    def all_entities(self):
        all_entities_list = list(self._entities)

        for hidden in self._hiddens:
            if len(hidden._entities) > 0:
                all_entities_list.extend(list(hidden._entities))

        return all_entities_list

    @property
    def all_solids(self):
        all_solids_list = list(self._world._solids)

        for hidden in self._hiddens:
            if len(hidden._solids) > 0:
                all_solids_list.extend(list(hidden._solids))

        for hidden in self._world._hiddens:
            if len(hidden._solids) > 0:
                all_solids_list.extend(list(hidden._solids))

        return all_solids_list

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

        self._child_nodes.append(node)
