class Tree:
    def __init__(self, root):
        self.root = root


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.children = []
        if parent != 0:
            parent.children.append(self)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def find_item(self, d):
        if self.data == d:
            return True

        for child in self.children:
            child.find_item(d)
