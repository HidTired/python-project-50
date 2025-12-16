from ..diff_representation import DiffNode

def render_stylish(diff_node, indent_level=0):
    def render_value(value):
        if isinstance(value, dict):
            return render_dict(value, indent_level + 1)
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, (int, float)):
            return str(value)
        else:
            return repr(value)[1:-1]  
    def render_dict(dct, level):
        lines = ['{' + ('\n' if dct else '')]
        for k, v in dct.items():
            space = ' ' * level * 4
            lines.append(space + f"{k}: {render_value(v)}")
        lines.append(' ' * ((level - 1) * 4) + "}")
        return '\n'.join(lines)

    result = []
    for child in diff_node.children:
        prefix = ' ' * indent_level * 4
        if child.action == '+':
            result.append(prefix + '+ ' + child.key + ': ' + render_value(child.new_value))
        elif child.action == '-':
            result.append(prefix + '- ' + child.key + ': ' + render_value(child.old_value))
        elif child.action == '~':
            result.append(prefix + '- ' + child.key + ': ' + render_value(child.old_value))
            result.append(prefix + '+ ' + child.key + ': ' + render_value(child.new_value))
        elif child.action == '=':
            result.append(prefix + '  ' + child.key + ': ' + render_value(child.old_value))
        elif child.action == '~' and len(child.children) > 0:
            result.append(prefix + child.key + ": ")
            result.extend(render_stylish(DiffNode(children=child.children), indent_level + 1).split('\n'))

    return "\n".join(result)