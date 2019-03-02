from math import trunc


class PriorityQueue:
    def __init__(self):
        self.data = MinHeap()

    def push(self, obj, prio):
        self.data.insert(obj, prio)

    def pop(self):
        return self.data.pop()

    def print(self):
        print("Pq data:")
        print(self.data)


class MinHeap:
    def __init__(self):
        self.i = 0
        self.data = []

    def __str__(self):
        return str(self.data)

    def print(self):
        return print(self.data)

    def get_parent(self, index):
        return self.data[trunc(index/2)]

    @staticmethod
    def get_left_child(index):
        return index * 2 + 1

    @staticmethod
    def get_right_child(index):
        return index * 2 + 2

    def get_min_child(self, index):
        l = self.get_left_child(index)
        r = self.get_right_child(index)
        if r > len(self.data):
            return l
        if self.data[l][1] < self.data[r][1]:
            return l
        if self.data[l][1] > self.data[r][1]:
            return r
        if self.data[l][1] == self.data[r][1]:
            if self.data[l][2] < self.data[r][2]:
                return l
            else:
                return r

    def insert(self, obj, prio):

        self.data.append([obj, prio, self.i])
        self.i = self.i + 1
        index = len(self.data) - 1

        while index != 0:
            if self.data[index][1] < self.data[trunc(index/2)][1]:
                d = self.data[index]
                self.data[index] = self.data[trunc(index/2)]
                self.data[trunc(index / 2)] = d
                index = trunc(index / 2)
            else:
                return

    def heapify(self, index):
        while index * 2 + 2 < len(self.data):
            m = self.get_min_child(index)
            if self.data[index][1] > self.data[m][1]:
                d = self.data[index]
                self.data[index] = self.data[m]
                self.data[m] = d
                index = m
            else:
                return

    def pop(self):
        if len(self.data) == 1:
            return self.data.pop()[0]
        result = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify(0)
        return result[0]
