import math
from typing import List, Dict


class MinHeap:
    def __init__(self, arr: List):
        self.arr = arr.copy()
        self._build_heap()

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        return "MinHeap(arr={})".format(self.arr)

    def __str__(self):
        return str(self.arr)

    def peek(self):
        return self.arr[0]

    def _heapify(self, node_index):
        children_nodes = self._get_children(node_index)
        temp_node = min(children_nodes, default=None, key=lambda n: n["value"])

        if temp_node is None or temp_node["value"] >= self.arr[node_index]:
            return

        temp_index = temp_node["index"]
        self.arr[node_index], self.arr[temp_index] = self.arr[temp_index], self.arr[node_index]

        self._heapify(temp_index)


    def _build_heap(self):
        last_parent = MinHeap._get_parent_index(len(self) - 1)

        for index in reversed(range(last_parent + 1)):
            self._heapify(index)


    def insert(self, value):
        self.arr.append(value)

        node_index = len(self.arr) - 1
        while node_index != 0:
            parent_index = self._get_parent_index(node_index)

            if self.arr[node_index] < self.arr[parent_index]:
                self.arr[node_index], self.arr[parent_index] = self.arr[parent_index], self.arr[node_index]

            node_index = parent_index

        return self.arr


    def remove(self):
        removed_element = self.arr[0]
        self.arr[0] = self.arr.pop()
        self._heapify(0)

        return removed_element

    def _get_children(self, node) -> List[Dict]:
        def create_node(index):
            return {"index": index, "value": self.arr[index]}

        children = []

        left_child = 2*node + 1
        if left_child < len(self):
            children.append(create_node(left_child))

        right_child = 2 * node + 2
        if right_child < len(self):
            children.append(create_node(right_child))

        return children

    @staticmethod
    def _get_parent_index(node_index):
        return math.floor((node_index - 1)/2)


if __name__ == "__main__":
    input_arr = [30, 102, 23, 12, 18, 9, 44, 17, 31]
    heap_obj = MinHeap(input_arr)

    print(heap_obj)
