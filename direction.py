from enum import Enum


class Direction(Enum):
    Left = 0
    Up = 1
    Right = 2
    Down = 3

    def __str__(self):
        if self.value == 0:
            return "left"
        if self.value == 1:
            return "Up"
        if self.value == 2:
            return "Right"
        if self.value == 3:
            return "Down"

