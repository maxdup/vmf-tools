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
            class_ = getattr(vmf, class_name)
            if class_:
                node = NodeParse(reader, class_)
                map.nodes.append(node)


def NodeParse(reader, class_):

    node = class_()
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
                except:
                    child_class_ = getattr(vmf, 'Node')
                child_node = NodeParse(reader, child_class_)
                node.child_nodes.append(child_node)

            else:
                break
            current_line = reader.readline()

    return node
