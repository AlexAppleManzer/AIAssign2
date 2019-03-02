from grid import Grid
from tree import Node
from pqueue import PriorityQueue

def solve(mode, grid):
    if mode == 1:
        print("sup")
        a = Grid([0, 1, 2, 3, 4, 5, 6, 7, 8])
        b = Grid([1, 2, 3, 8, 0, 4, 7, 6, 5])
        c = Grid([0, 1, 2, 3, 4, 5, 6, 7, 8])

        print(a)
        print(b)
        print(c)
        print("a = b? %s" % a.equals(b))
        print("a = c? %s" % a.equals(c))
        print("a = c? %s" % Grid.equal(a, c))
        print("is a soln? %s" % a.is_solution())
        print("is b soln? %s" % b.is_solution())

    if mode == 2:
        a = Node(Grid([0, 1, 2, 3, 4, 5, 6, 7, 8]), 0)
        b = Node(a.data, a)
        a.print_tree()

    if mode == 3:
        a = Node(Grid(grid), 0)
        a.print_tree()
        for move in a.data.get_moves():
            print(move)
            Node(Grid(a.data.move(move)), a)
        a.print_tree()

    if mode == 4:
        pq = PriorityQueue()
        root = Node(Grid(grid), 0)

        def expand_node(node):
            if len(node.children) == 0:
                for move in node.data.get_moves():
                    m = node.data.move(move)
                    if not move == root.find_item(move):
                        print("nice")
                        Node(Grid(m), node)

        if root.data.is_solution():
            return

        pq.push(root, 0)

        for i in range(999):
            nxt = pq.pop()
            expand_node(nxt)
            for child in nxt.children:
                pq.push(child, child.data.h_score())
                if child.data.is_solution():
                    print("done")
                    root.print_tree()
                    return
                pq.print()
                print("printing child")
                child.print_tree()





