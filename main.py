# Course: CS4242
# Student name: Alex Manzer
# Student ID: 827565
# Assignment #: #2
# Due Date: 3/5/2019
# Signature: ______________
# Score: _____________

from eightpuzzlegui import EightPuzzleGUI
from eightpuzzlelogic import solve
from pqueue import PriorityQueue
from cube import Cube
from random import randint
from copy import deepcopy
from tree import Node
from face import Facing
import tkinter as tk
from eightpuzzlelogic import B


def solve_cube():

    def expand_node(node):
        # expands node to generate all possible moves
        if len(node.children) == 0:
            for i in range(6):
                m = deepcopy(node.data)
                m.rotate_face(list(Facing)[i])
                if not root.find_item(m):
                    # makes sure there are no duplicates
                    Node(m, node, list(Facing)[i])

    def increment(button, button1):
        gui.mainFrame.update()
        nxt = pq.pop()  # gets next thing in PQ
        expand_node(nxt)
        # print(nxt.data)

        if len(pq) > 0:
            gui.draw_cube(pq.data.data[0][0].data, gui.rightFrame1, 10)
        if len(pq) > 1:
            gui.draw_cube(pq.data.data[1][0].data, gui.rightFrame2, 10)
        if len(pq) > 2:
            gui.draw_cube(pq.data.data[2][0].data, gui.rightFrame3, 10)
        if len(pq) > 3:
            gui.draw_cube(pq.data.data[3][0].data, gui.rightFrame4, 10)
        if len(pq) > 4:
            gui.draw_cube(pq.data.data[4][0].data, gui.rightFrame5, 10)

        for child in nxt.children:
            # adds children to PQ with h(n) + g(n)
            # gui.draw_grid(child.data, gui.mainFrame, 40)
            if child.data.h_score() < best.data.data.h_score():
                best.data = child
                gui.draw_grid(best.data.data, gui.mainFrame, 40)
            pq.push(child, child.data.h_score() + 4 * child.level)
            if child.data.h_score() == 0:
                button.destroy()
                button1.destroy()
                # print(child.data)
                # print(child.moves)
                # print("done idiot")

                gui.draw_moves(child.moves)
                return True
            # pq.print()
        return False

    def loop_to_end(button, button1):
        for i in range(999):
            if increment(button, button1):
                return

    pq = PriorityQueue()
    root = Node(Cube(), 0, -1)
    root.data.scramble(6)
    # print(root.data)

    gui = EightPuzzleGUI()

    pq.push(root, 0)
    best = B(root)

    start = tk.Button(gui.root, text="Increment", command=lambda: increment(start, loop), width=5, height=5)
    start.grid(column=0, row=4, sticky=tk.N + tk.S + tk.E + tk.W)

    loop = tk.Button(gui.root, text="Loop", command=lambda: loop_to_end(start, loop), width=5, height=5)
    loop.grid(column=1, row=4, sticky=tk.N + tk.S + tk.E + tk.W)

    gui.root.mainloop()


def test_rotate():
    # tests rotate functions in Cube class
    c = Cube()
    print(c)
    m = []
    for i in range(9):
        rand = randint(0, 5)
        if rand == 0:
            m.append(0)
            c.rotate_r()
        if rand == 1:
            m.append(1)
            c.rotate_l()
        if rand == 2:
            m.append(2)
            c.rotate_u()
        if rand == 3:
            m.append(3)
            c.rotate_d()
        if rand == 4:
            m.append(4)
            c.rotate_f()
        if rand == 5:
            m.append(5)
            c.rotate_b()

    for i in range(9):
        nxt = m.pop()
        if nxt == 1:
            c.rotate_r()
        if nxt == 0:
            c.rotate_l()
        if nxt == 3:
            c.rotate_u()
        if nxt == 2:
            c.rotate_d()
        if nxt == 5:
            c.rotate_f()
        if nxt == 4:
            c.rotate_b()

    print(c)


if __name__ == "__main__":
    solve_cube()
    solve(4)
