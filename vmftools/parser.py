from . import vmf
from vmftools.property_parsers import *
from vmftools.nodes import *
from fgdtools import FgdParse


def VmfParse(map_file, fgd_file=None):

    if fgd_file:
        fgd = FgdParse(fgd_file)
    else:
        fgd = None

    reader = open(map_file, "r")
    map = vmf.VMF()

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
            try:
                class_ = getattr(vmf, class_name)
                node = class_()
            except:
                class_ = getattr(vmf, 'Node')
                node = vmf.Node(class_name)

            NodeParse(reader, node, map, fgd)

    return map


def NodeParse(reader, node, parent_node, fgd=None):

    current_line = reader.readline()

    properties = {}

    while '}' not in current_line:

        if not current_line.strip():
            current_line = reader.readline()
            continue

        if '"' in current_line:
            p_args = current_line.strip().strip('"').split('"')
            properties[p_args[0]] = p_args[-1]
            current_line = reader.readline()
            continue

        child_class_name = ''
        while '{' not in current_line:
            child_class_name += current_line
            current_line = reader.readline()

        curr_split = current_line.split("{", 1)
        child_class_name = child_class_name.strip() + ' ' + \
            curr_split[0].strip()
        child_class_name = child_class_name.strip()
        current_line = curr_split[1]

        if child_class_name:
            try:
                child_class_ = getattr(vmf, child_class_name)
                child_node = child_class_()
            except:
                child_node = vmf.Node(child_class_name)

            NodeParse(reader, child_node, node, fgd)

        else:
            break
        current_line = reader.readline()

    schema = node.SCHEMA
    if fgd and 'classname' in properties:
        model = fgd.get_entity_by_name(properties['classname'])
        if (model):
            schema = dict(schema, **model.property_schema)
            schema['classname'] = properties['classname']

    if not isinstance(node, connections):
        obj_properties = parse_properties(properties, schema, node.FALLBACK)
        for k, v in obj_properties.items():
            node.add_property(k, v)

    parent_node.add_child(node)
    return node
