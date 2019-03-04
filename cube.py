
# Face:
# |00 01|
# |10 11|
# R L U D F B


class Face:
    def __init__(self, num):
        self.data = [[num, num], [num, num]]

    def __getitem__(self, item):
        return self.data[item]


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

    def rotate_r(self):
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



