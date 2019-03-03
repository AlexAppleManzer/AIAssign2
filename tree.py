class Tree:
    def __init__(self, root):
        self.root = root


class Node:

    def __init__(self, data, parent, move):
        self.moves = []
        self.data = data
        self.children = []
        if parent != 0:
            parent.children.append(self)
            self.level = parent.level + 1
            self.moves = parent.moves[:]
            self.moves.append(move)
        else:
            self.level = 0

    def print_tree(self):
        # prints tree in depth first order
        print(self.data)
        for child in self.children:
            child.print_tree()

    def find_item(self, d):
        # finds item in tree
        if self.data == d:
            return True

        for child in self.children:
            child.find_item(d)
