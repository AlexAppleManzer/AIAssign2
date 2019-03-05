from face import Facing
from random import choice
# Face:
# |00 01|
# |10 11|
# R L U D F B


class Face:
    def __init__(self, num):
        self.data = [[num, num], [num, num]]

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        return " |%d %d|\n |%d %d|" % (self.data[0][0], self.data[0][1], self.data[1][0], self.data[1][1])


class Cube:

    def __init__(self):
        # 6 arrays with 4 elements
        # Right, Left, Up, Down, Front, Back - Enum Face
        self.Right = Face(0)
        self.Left = Face(1)
        self.Up = Face(2)
        self.Down = Face(3)
        self.Front = Face(4)
        self.Back = Face(5)
        self.faces = [self.Right, self.Left, self.Up, self.Down, self.Front, self.Back]

    def __eq__(self, other):
        for i in range(len(self.faces)):
            if self.faces[i][0][0] != other.faces[i][0][0]:
                return False
            if self.faces[i][0][1] != other.faces[i][0][0]:
                return False
            if self.faces[i][1][0] != other.faces[i][0][0]:
                return False
            if self.faces[i][1][1] != other.faces[i][0][0]:
                return False
        return True

    def __str__(self):
        # string output command
        result = "score = %d\n" % self.h_score() + str(self.Back) + "\n" + str(self.Up)
        result += "\n|{} {}|{} {}|{} {}|".format(self.Left[0][0], self.Left[0][1],
                                               self.Front[0][0], self.Front[0][1],
                                               self.Right[0][0], self.Right[0][1])
        result += "\n|{} {}|{} {}|{} {}|".format(self.Left[1][0], self.Left[1][1],
                                               self.Front[1][0], self.Front[1][1],
                                               self.Right[1][0], self.Right[1][1])
        result += "\n" + str(self.Down)
        return result

    def rotate_r(self):
        # rotate right face
        temp = self.Right[0][0]
        self.Right[0][0] = self.Right[1][0]
        self.Right[1][0] = self.Right[1][1]
        self.Right[1][1] = self.Right[0][1]
        self.Right[0][1] = temp

        temp = [self.Front[0][1], self.Front[1][1]]
        self.Front[0][1] = self.Down[0][1]
        self.Front[1][1] = self.Down[1][1]
        self.Down[0][1] = self.Back[0][1]
        self.Down[1][1] = self.Back[1][1]
        self.Back[0][1] = self.Up[0][1]
        self.Back[1][1] = self.Up[1][1]
        self.Up[0][1] = temp[0]
        self.Up[1][1] = temp[1]

    def rotate_l(self):
        # rotate left face
        temp = self.Right[0][1]
        self.Right[0][1] = self.Right[1][1]
        self.Right[1][1] = self.Right[1][0]
        self.Right[1][0] = self.Right[0][0]
        self.Right[0][0] = temp

        temp = [self.Back[0][1], self.Back[1][1]]
        self.Back[1][1] = self.Down[1][1]
        self.Back[0][1] = self.Down[0][1]
        self.Down[1][1] = self.Front[1][1]
        self.Down[0][1] = self.Front[0][1]
        self.Front[1][1] = self.Up[1][1]
        self.Front[0][1] = self.Up[0][1]
        self.Up[0][1] = temp[0]
        self.Up[1][1] = temp[1]

    def rotate_u(self):
        # rotate up face
        temp = self.Up[0][0]
        self.Up[0][0] = self.Up[1][0]
        self.Up[1][0] = self.Up[1][1]
        self.Up[1][1] = self.Up[0][1]
        self.Up[0][1] = temp

        temp = [self.Right[0][1], self.Right[0][0]]
        self.Right[0][1] = self.Back[1][0]
        self.Right[0][0] = self.Back[1][1]
        self.Back[1][0] = self.Left[0][1]
        self.Back[1][1] = self.Left[0][0]
        self.Left[0][1] = self.Front[0][1]
        self.Left[0][0] = self.Front[0][0]
        self.Front[0][1] = temp[0]
        self.Front[0][0] = temp[1]

    def rotate_d(self):
        # rotate down face
        temp = self.Up[0][1]
        self.Up[0][1] = self.Up[1][1]
        self.Up[1][1] = self.Up[1][0]
        self.Up[1][0] = self.Up[0][0]
        self.Up[0][0] = temp

        temp = [self.Front[0][1], self.Front[0][0]]
        self.Front[0][0] = self.Left[0][0]
        self.Front[0][1] = self.Left[0][1]
        self.Left[0][0] = self.Back[1][1]
        self.Left[0][1] = self.Back[1][0]
        self.Back[1][1] = self.Right[0][0]
        self.Back[1][0] = self.Right[0][1]
        self.Right[0][0] = temp[1]
        self.Right[0][1] = temp[0]

    def rotate_f(self):
        # rotate front face
        temp = self.Front[0][0]
        self.Front[0][0] = self.Front[1][0]
        self.Front[1][0] = self.Front[1][1]
        self.Front[1][1] = self.Front[0][1]
        self.Front[0][1] = temp

        temp = [self.Right[1][0], self.Right[0][0]]
        self.Right[1][0] = self.Up[1][1]
        self.Right[0][0] = self.Up[1][0]
        self.Up[1][1] = self.Left[0][1]
        self.Up[1][0] = self.Left[1][1]
        self.Left[0][1] = self.Down[0][0]
        self.Left[1][1] = self.Down[0][1]
        self.Down[0][0] = temp[0]
        self.Down[0][1] = temp[1]

    def rotate_b(self):
        # rotate back face
        temp = self.Front[0][1]
        self.Front[0][1] = self.Front[1][1]
        self.Front[1][1] = self.Front[1][0]
        self.Front[1][0] = self.Front[0][0]
        self.Front[0][0] = temp

        temp = [self.Down[0][0], self.Down[0][1]]
        self.Down[0][0] = self.Left[0][1]
        self.Down[0][1] = self.Left[1][1]
        self.Left[0][1] = self.Up[1][1]
        self.Left[1][1] = self.Up[1][0]
        self.Up[1][1] = self.Right[1][0]
        self.Up[1][0] = self.Right[0][0]
        self.Right[1][0] = temp[0]
        self.Right[0][0] = temp[1]

    def rotate_face(self, facing):
        # rotate any face using Facing enum
        if facing == Facing.R:
            self.rotate_r()
        if facing == Facing.L:
            self.rotate_l()
        if facing == Facing.U:
            self.rotate_u()
        if facing == Facing.D:
            self.rotate_d()
        if facing == Facing.F:
            self.rotate_f()
        if facing == Facing.B:
            self.rotate_b()

    def h_score(self):
        # calculate heuristic score
        return self.face_score()

    def face_score(self):
        score = 0
        for i in range(6):
            if self.faces[i][0][0] != i:
                score += 1
            if self.faces[i][0][1] != i:
                score += 1
            if self.faces[i][1][0] != i:
                score += 1
            if self.faces[i][1][1] != i:
                score += 1
        return score

    def scramble(self, num):
        # scrambles cube num rotations
        for i in range(num):
            self.rotate_face(choice(list(Facing)))

