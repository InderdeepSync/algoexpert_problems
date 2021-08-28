from heap import Heap

class ContinuousMedianHandler:
    def __init__(self):
        self.min_heap = Heap([], is_min_heap=True)
        self.max_heap = Heap([], is_min_heap=False)

    def add_number(self, item):
        if len(self.max_heap) == 0 or item <= self.max_heap.peek():
            self.max_heap.insert(item)
        else:
            self.min_heap.insert(item)

        if len(self.min_heap) - len(self.max_heap) == 2:
            self.max_heap.insert(self.min_heap.remove())
        elif len(self.max_heap) - len(self.min_heap) == 2:
            self.min_heap.insert(self.max_heap.remove())

        if len(self.min_heap) == len(self.max_heap):
            median = (self.min_heap.peek() + self.max_heap.peek())/2
        elif len(self.min_heap) < len(self.max_heap):
            median = self.max_heap.peek()
        else:
            median = self.min_heap.peek()

        return median


if __name__ == "__main__":
    pass
    # print("Continuous Median: {}".format(continuous_median([1, 4, 9])))