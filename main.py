
from eightpuzzlegui import EightPuzzleGUI
from eightpuzzlelogic import solve
from pqueue import PriorityQueue
from cube import Cube
from random import randint
from copy import deepcopy
from tree import Node

if __name__ == "__main__":
    c = Cube()
    d = deepcopy(c)
    d.rotate_f()
    print(c)
    solve(4)


def solve_cube():
    root = Node(Cube(), 0, -1)
    root.data.scramble(10)

    def expand_node(node):
        # expands node to generate all possible moves

        if len(node.children) == 0:
            for i in range(6):
                m = deepcopy(node.data)
                m.rotate_face(i)
                if not root.find_item(m):
                    # makes sure there are no duplicates
                    Node(Grid(m), node, i)


def test_rotate():

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