from ..scripts.diff_representation import DiffNode

def render_stylish(diff_node, indent_level=0):
    def render_value(value):
        if isinstance(value, dict):
            return render_dict(value, indent_level + 1)
        elif isinstance(value, bool):
            return str(value).lower() 
        elif value is None:
            return 'null' 
        elif isinstance(value, (int, float)):
            return str(value)
        else:
            return repr(value)[1:-1]  

    def render_dict(dct, level):
        lines = []
        space = ' ' * level * 4
        lines.append(space + '{')
        for k, v in dct.items():
            inner_space = ' ' * (level + 1) * 4
            lines.append(inner_space + f"{k}: {render_value(v)}")
        lines.append(space + '}')
        return '\n'.join(lines)

    result = []
    for child in diff_node.children:
        prefix = ' ' * indent_level * 4
        if child.action == 'added':
            result.append(prefix + '+ ' + child.key + ': ' + render_value(child.new_value))
        elif child.action == 'deleted':
            result.append(prefix + '- ' + child.key + ': ' + render_value(child.old_value))
        elif child.action == 'unchanged':
            result.append(prefix + '  ' + child.key + ': ' + render_value(child.old_value))
        elif child.action == 'changed':
            result.append(prefix + '- ' + child.key + ': ' + render_value(child.old_value))
            result.append(prefix + '+ ' + child.key + ': ' + render_value(child.new_value))
        elif child.action == 'nested':
            block = render_stylish(DiffNode(children=child.children), indent_level + 1)
            result.append(prefix + child.key + ": " + block)

    outer_indent = ' ' * indent_level * 4
    wrapped_result = [
        outer_indent + '{',
        *(line.rstrip() for line in result),
        outer_indent + '}',
    ]
    return '\n'.join(wrapped_result)