# Course: CS4242
# Student name: Alex Manzer
# Student ID: 827565
# Assignment #: #2
# Due Date: 3/5/2019
# Signature: ______________
# Score: _____________

from eightpuzzlegui import EightPuzzleGUI
from pqueue import PriorityQueue
from cube import Cube
from random import randint
from copy import deepcopy
from tree import Node
from face import Facing
from grid import Grid
import tkinter as tk
from random import choice
from random import random
import math

class B():
    # class to store variable scoping, that's it
    def __init__(self, node):
        self.data = node


def solve_cube_SA():
    # SA search algorithm

    def accept_probability(old, new, temperature):
        if new < old:
            return 1

        return math.exp((old - new) / temperature)

    gui = EightPuzzleGUI()

    def solve():

        current = Cube()
        current.scramble(3)
        currentScore = current.h_score()
        temp = 10000
        coolingRate = 0.003
        moves = []

        while temp > 1:

            gui.draw_cube(current, gui.mainFrame, 50)

            move = choice(list(Facing))
            newGrid = deepcopy(current)
            newGrid.rotate_face(move)

            if currentScore == 0:
                gui.draw_moves(moves)
                return True

            newScore = newGrid.h_score()
            if accept_probability(currentScore, newScore, temp) > random():
                current = newGrid
                currentScore = newScore
                moves.append(move)
                gui.draw_cube(current, gui.mainFrame, 50)
                gui.mainFrame.update()

            temp = temp * (1 - coolingRate)

    start = tk.Button(gui.root, text="Solve", command=lambda: solve(), width=5, height=5)
    start.grid(column=0, row=4, sticky=tk.N + tk.S + tk.E + tk.W)

    gui.root.mainloop()


def solve_eight_puzzle_SA():
    # SA search algorithm

    def accept_probability(old, new, temperature):
        if new < old:
            return 1

        return math.exp((old - new) / temperature)

    gui = EightPuzzleGUI()

    def solve():

        current = Grid([2, 8, 3, 1, 6, 4, 7, 0, 5])
        currentScore = current.h_score()
        temp = 10000
        coolingRate = 0.003
        moves = []

        while temp > 1:

            gui.draw_grid(current, gui.mainFrame, 50)

            move = choice(current.get_moves())
            newGrid = Grid(current.move(move))

            if currentScore == 0:
                gui.draw_moves(moves)
                return True

            newScore = newGrid.h_score()
            if accept_probability(currentScore, newScore, temp) > random():
                current = newGrid
                currentScore = newScore
                moves.append(move)
                gui.draw_grid(current, gui.mainFrame, 50)
                gui.mainFrame.update()

            temp = temp * (1 - coolingRate)

    start = tk.Button(gui.root, text="Solve", command=lambda: solve(), width=5, height=5)
    start.grid(column=0, row=4, sticky=tk.N+tk.S+tk.E+tk.W)

    gui.root.mainloop()

if __name__ == "__main__":
    solve_cube_SA()
