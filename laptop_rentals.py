from typing import List

from heap import MinHeap

class Duration:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def __ge__(self, other):
        return self.end >= other.end

    def __repr__(self):
        return "({}, {})".format(self.start, self.end)

def laptop_rentals_via_heap(arr: List[Duration]):
    if len(arr) == 0:
        return 0

    arr.sort(key=lambda d: d.start)
    heap_obj = MinHeap(arr[:1])

    for index in range(1, len(arr)):
        if arr[index].start < heap_obj.peek().end:
            pass
        else:
            heap_obj.remove()

        heap_obj.insert(arr[index])

    return len(heap_obj)


def laptop_rentals_special_trick(arr):
    temp = list(zip(*arr))
    start_times = sorted(temp[0])
    end_times = sorted(temp[1])
    start = end = 0
    max_laptops_required = 0
    current_laptops_needed = 0
    while start < len(start_times) and end < len(end_times):
        if start_times[start] < end_times[end]:
            current_laptops_needed += 1
            start += 1
        else:
            current_laptops_needed -= 1
            end += 1
        max_laptops_required = max(max_laptops_required, current_laptops_needed)

    return max_laptops_required




if __name__ == "__main__":
    input_arr = [[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]
    print("Laptop Rentals(Heap): {}".format(laptop_rentals_via_heap(list(map(lambda t: Duration(t[0], t[1]), input_arr)))))
    print("Laptop Rentals(Special): {}".format(laptop_rentals_special_trick(input_arr)))