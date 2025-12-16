class DiffNode:
    def __init__(self, key=None, old_value=None, new_value=None, action=None, children=None):
        self.key = key
        self.old_value = old_value
        self.new_value = new_value
        self.action = action  # Возможные варианты: '+', '-', '=', '~'
        self.children = children or []

    def append_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"<DiffNode({self.key}, {self.old_value}, {self.new_value}, {self.action})>"