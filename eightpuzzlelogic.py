from grid import Grid
from tree import Node
from pqueue import PriorityQueue
from random import choice

def solve(mode):
    if mode == 1:
        # test code for grid class
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
        # test code for node class
        a = Node(Grid([0, 1, 2, 3, 4, 5, 6, 7, 8]), 0)
        b = Node(a.data, a)
        a.print_tree()

    if mode == 3:
        # test code for get_moves()
        soln = Grid([1, 2, 3, 8, 0, 4, 7, 6, 5])
        a = Node(generate_problem(soln), 0)
        a.print_tree()
        for move in a.data.get_moves():
            print(move)
            Node(Grid(a.data.move(move)), a)
        a.print_tree()

    if mode == 4:
        # A* search algorithm
        pq = PriorityQueue()
        soln = Grid([1, 2, 3, 8, 0, 4, 7, 6, 5])
        root = Node(generate_problem(soln), 0)

        def expand_node(node):
            # expands node to generate all possible moves
            if len(node.children) == 0:
                for move in node.data.get_moves():
                    m = node.data.move(move)
                    if not move == root.find_item(move):
                        # makes sure there are no duplicates
                        Node(Grid(m), node)

        if root.data.is_solution():
            return

        pq.push(root, 0)

        for i in range(99999):
            # loops until solution is found
            nxt = pq.pop() # gets next thing in PQ
            expand_node(nxt)
            for child in nxt.children:
                # adds children to PQ with h(n) + g(n)
                pq.push(child, child.data.h_score() + child.level)
                if child.data.is_solution():
                    print("done")
                    root.print_tree()
                    return
                pq.print()
                print("printing child")
                child.print_tree()


def generate_problem(g):
    # randomly scrambles
    for i in range(50):
        m = g.get_moves()
        g.data = g.move(choice(m))
    return g
