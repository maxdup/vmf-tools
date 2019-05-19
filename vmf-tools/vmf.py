import importlib

namespace = __import__(__name__)


class VMF():

    nodes = []

    def __init__(self, file):

        reader = open(file, "r")

        eof = False

        while not eof:
            class_name = ''
            current_line = reader.readline()

            if not current_line:
                eof = True
                break

            while '{' not in current_line:
                class_name += current_line
                current_line = reader.readline()

            class_name = class_name.strip()
            if class_name:
                class_ = getattr(namespace, class_name)
                if class_:
                    self.nodes.append(class_(reader))


class Node:

    def __init__(self, reader):
        self.properties = {}
        self.child_nodes = []
        self.p_args = []
        current_line = reader.readline()

        while '}' not in current_line:

            while '"' in current_line:
                self.p_args = current_line.strip().strip('"').split('"')
                self.properties[self.p_args[0]] = self.p_args[-1]

                current_line = reader.readline()

            while '}' not in current_line:
                child_class_name = ''
                while '{' not in current_line:
                    child_class_name += current_line
                    current_line = reader.readline()

                child_class_name = child_class_name.strip()

                if child_class_name:
                    try:
                        child_class_ = getattr(
                            namespace, child_class_name.strip())
                        self.child_nodes.append(child_class_(reader))
                    except:
                        self.child_nodes.append(Node(reader))

                else:
                    break
                current_line = reader.readline()

        return


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
