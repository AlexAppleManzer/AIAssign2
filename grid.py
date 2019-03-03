# grid class: represents 3x3 grid board state
# uses numbers 0-8, where 0 represents the blank tile
# ex: [0, 1, 2, 3, 4, 5, 6, 7, 8] =
# |0 1 2|
# |3 4 5|
# |6 7 8|

from direction import Direction


class Grid:

    def __init__(self, data):
        self.data = data
        self.soln = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        result = "["
        i = 0
        for item in self.data:

            result = result + "%d, " % item
            if i == 2 or i == 5:
                result += "\n "
            i += 1

        return result[:-2] + "] Score:" + str(self.h_score())

    def get_blank(self):
        # returns index location of blank tile
        for index, item in enumerate(self.data):
            if item == 0:
                return index
        return -1

    def get_moves(self):
        # returns the possible moves the blank space could go
        moves = []
        bkpos = self.get_blank()

        if bkpos > 2:
            moves.append(Direction.Up)

        if bkpos < 6:
            moves.append(Direction.Down)

        if bkpos != 0 and bkpos != 3 and bkpos != 6:
            moves.append(Direction.Left)

        if bkpos != 2 and bkpos != 5 and bkpos != 8:
            moves.append(Direction.Right)

        return moves

    def move(self, dir):
        # moves in direction given from Direction enum
        if dir == Direction.Up:
            return self.move_up()
        if dir == Direction.Down:
            return self.move_down()
        if dir == Direction.Left:
            return self.move_left()
        if dir == Direction.Right:
            return self.move_right()

    def move_up(self):
        # returns grid after an up move
        bkpos = self.get_blank()
        assert (bkpos > 2)
        result = self.data[:]
        result[bkpos] = result[bkpos - 3]
        result[bkpos - 3] = 0
        return result

    def move_down(self):
        # returns grid after an up move
        bkpos = self.get_blank()
        assert (bkpos < 6)
        result = self.data[:]
        result[bkpos] = result[bkpos + 3]
        result[bkpos + 3] = 0
        return result

    def move_left(self):
        # returns grid after an up move
        bkpos = self.get_blank()
        assert (bkpos != 0 and bkpos != 3 and bkpos != 6)
        result = self.data[:]
        result[bkpos] = result[bkpos - 1]
        result[bkpos - 1] = 0
        return result

    def move_right(self):
        # returns grid after an up move
        bkpos = self.get_blank()
        assert (bkpos != 2 and bkpos != 5 and bkpos != 8)
        result = self.data[:]
        result[bkpos] = result[bkpos + 1]
        result[bkpos + 1] = 0
        return result

    def is_solution(self):
        # checks if current grid is solution
        if self.data == self.soln:
            return True
        return False

    def equals(self, g):
        if self.data == g.data:
            return True
        return False

    def h_score(self):
        # determines heuristic score based on manhattan distance

        def get_row(j):
            return int(j / 3)

        def get_col(j):
            return j % 3

        def soln_index(num):
            j = 0
            for j in range(9):
                if num == self.soln[j]:
                    return j

        score = 0
        for i in range(9):
            row = get_row(i)
            col = get_col(i)
            score += abs(row - get_row(soln_index(self.data[i])))
            score += abs(col - get_col(soln_index(self.data[i])))

        return score

    @staticmethod
    def equal(g1, g2):
        if g1.data == g2.data:
            return True
        return False
