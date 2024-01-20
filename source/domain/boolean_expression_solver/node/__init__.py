class Node:
    def __init__(self, value: str = ""):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return (
                self.value == other.value and
                self.left == other.left and
                self.right == other.right
        )

    def __repr__(self, level=0, connector="", completed_levels=None):
        completed_levels = completed_levels if completed_levels else []
        tree_str = f"{self.get_indent(level, completed_levels)}{connector}{self.value}\n"
        if self.left:
            tree_str += self.left.__repr__(level + 1, connector="├── ", completed_levels=completed_levels)
        if self.right:
            completed_levels.append(level)
            tree_str += self.right.__repr__(level + 1, connector="└── ", completed_levels=completed_levels)
        if level in completed_levels:
            completed_levels.remove(level)
        return tree_str

    @staticmethod
    def get_indent(level, completed_levels):
        return "".join("     " if i in completed_levels else "│    " for i in range(level - 1))
