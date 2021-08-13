import math

class MinMaxStack:

    def __init__(self):
        self.arr = []

    def __repr__(self):
        return "MinMaxStack(arr={})".format(list(map(lambda x: x["value"], self.arr)))

    def push(self, value):
        self.arr.insert(0, {"value": value, "min": min(self.min_value, value), "max": max(self.max_value, value)})

    def pop(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    @property
    def min_value(self):
        try:
            return self.peek()["min"]
        except IndexError:
            return math.inf

    @property
    def max_value(self):
        try:
            return self.peek()["max"]
        except IndexError:
            return -math.inf