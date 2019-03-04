from grid import Grid
from tree import Node
from pqueue import PriorityQueue
from random import choice
import tkinter as tk
from eightpuzzlegui import EightPuzzleGUI

class B():
    def __init__(self, node):
        self.data = node

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
        a = Node(Grid([0, 1, 2, 3, 4, 5, 6, 7, 8]), 0, 0)
        b = Node(a.data, a, 0)
        a.print_tree()

    if mode == 3:
        # test code for get_moves()
        soln = Grid([1, 2, 3, 8, 0, 4, 7, 6, 5])
        a = Node(generate_problem(soln), 0, 0)
        a.print_tree()
        for move in a.data.get_moves():
            print(move)
            Node(Grid(a.data.move(move)), a, 0)
        a.print_tree()

    if mode == 4:
        # A* search algorithm
        pq = PriorityQueue()
        soln = Grid([1, 2, 3, 8, 0, 4, 7, 6, 5])
        root = Node(generate_problem(soln), 0, 0)

        def expand_node(node):
            # expands node to generate all possible moves
            if len(node.children) == 0:
                for move in node.data.get_moves():
                    m = Grid(node.data.move(move))
                    if not root.find_item(m):
                        # makes sure there are no duplicates
                        Node(m, node, move)

        if root.data.is_solution():
            return

        pq.push(root, 0)

        gui = EightPuzzleGUI()
        best = B(root)
        gui.draw_grid(best.data.data, gui.mainFrame, 50)

        def increment(button, button1):
            gui.mainFrame.update()
            nxt = pq.pop() # gets next thing in PQ
            expand_node(nxt)

            if len(pq) > 0:
                gui.draw_grid(pq.data.data[0][0].data, gui.rightFrame1, 12)
            if len(pq) > 1:
                gui.draw_grid(pq.data.data[1][0].data, gui.rightFrame2, 12)
            if len(pq) > 2:
                gui.draw_grid(pq.data.data[2][0].data, gui.rightFrame3, 12)
            if len(pq) > 3:
                gui.draw_grid(pq.data.data[3][0].data, gui.rightFrame4, 12)
            if len(pq) > 4:
                gui.draw_grid(pq.data.data[4][0].data, gui.rightFrame5, 12)

            for child in nxt.children:
                # adds children to PQ with h(n) + g(n)
                # gui.draw_grid(child.data, gui.mainFrame, 50)
                if child.data.h_score() < best.data.data.h_score():
                    best.data = child
                    gui.draw_grid(best.data.data, gui.mainFrame, 50)
                pq.push(child, child.data.h_score() + 0.5 * child.level)
                if child.data.is_solution():
                    button.destroy()
                    button1.destroy()
                    # print(child.moves)
                    gui.draw_moves(child.moves)
                    return True
                # pq.print()
            return False

        def loop_to_end(button, button1):
            # loops until solution is found
            while True:
                if increment(button, button1):
                    return

        start = tk.Button(gui.root, text="Increment", command=lambda: increment(start, loop), width=5, height=5)
        start.grid(column=0, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

        loop = tk.Button(gui.root, text="Loop", command=lambda: loop_to_end(start, loop), width=5, height=5)
        loop.grid(column=1, row=4, sticky=tk.N + tk.S + tk.E + tk.W)

        gui.root.mainloop()


def generate_problem(g):
    # randomly scrambles
    for i in range(50):
        m = g.get_moves()
        g.data = g.move(choice(m))
    return g
