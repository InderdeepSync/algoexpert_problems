class MinMaxStack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        if self.arr:
            min_value = min(self.arr[-1]["min"], value)
            max_value = max(self.arr[-1]["max"], value)
        else:
            min_value, max_value = value, value

        self.arr.append({"value": value, "min": min_value, "max": max_value})

    def pop(self):
        self.arr.pop()

    def peek(self):
        return self.arr[-1]

