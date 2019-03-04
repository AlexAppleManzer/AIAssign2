from enum import Enum


class Facing(Enum):
    R = 0  # right face
    L = 1  # Left face
    U = 2  # up face
    D = 3  # Down Face
    F = 4  # Front Face
    B = 5  # Back Face

    def __str__(self):
        if self.value == 0:
            return "R"
        if self.value == 1:
            return "L"
        if self.value == 2:
            return "U"
        if self.value == 3:
            return "D"
        if self.value == 4:
            return "F"
        if self.value == 5:
            return "B"


class Direction(Enum):

    c = 0  # (clockwise)
    i = 1  # Inverse (counter clockwise)

    def __str__(self):
        if self.value == 0:
            return ""
        if self.value == 1:
            return "i"
