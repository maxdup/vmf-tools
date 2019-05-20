from . import vmf


def VmfParse(file):

    reader = open(file, "r")

    eof = False
    map = vmf.VMF()

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
            try:
                class_ = getattr(vmf, class_name)
                node = class_()
            except:
                class_ = getattr(vmf, 'Node')
                node = vmf.Node(class_name)

            NodeParse(reader, node)

            if class_name == 'versioninfo':
                map.versioninfo = node
            elif class_name == 'visgroups':
                map.visgroups = node
            elif class_name == 'viewsettings':
                map.visgroups = node
            elif class_name == 'world':
                map.visgroups = node
            elif class_name == 'entity':
                map.entities.append(node)
            elif class_name == 'cameras':
                map.cameras = node
            elif class_name == 'cordon':
                map.cordon = node


def NodeParse(reader, node):

    current_line = reader.readline()

    while '}' not in current_line:

        while '"' in current_line:
            p_args = current_line.strip().strip('"').split('"')
            node.properties[p_args[0]] = p_args[-1]

            current_line = reader.readline()

        while '}' not in current_line:
            child_class_name = ''
            while '{' not in current_line:
                child_class_name += current_line
                current_line = reader.readline()

            child_class_name = child_class_name.strip()

            if child_class_name:
                try:
                    child_class_ = getattr(vmf, child_class_name.strip())
                    child_node = child_class_()
                except:
                    child_node = vmf.Node(child_class_name)

                NodeParse(reader, child_node)
                node.child_nodes.append(child_node)

            else:
                break
            current_line = reader.readline()

    return node
