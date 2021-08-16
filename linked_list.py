class Node:
    def __init__(self, value, nexxt=None):
        self.value = value
        self.next = nexxt

    def __repr__(self):
        return "Node(value={}, next={})".format(self.value, self.next)

    def __str__(self):
        return repr(self)

    def __len__(self):
        if not self.next:
            return 1
        return 1 + len(self.next)


def remove_duplicates_from_sorted_list(linked_list):
    initial = linked_list

    parent = linked_list
    linked_list = linked_list.next

    while linked_list:
        if linked_list.value == parent.value:
            temp = linked_list

            parent.next = linked_list.next
            linked_list = linked_list.next

            temp.next = None
            continue

        parent = linked_list
        linked_list = linked_list.next

    return initial

def shift_linked_list(linked_list: Node, k):
    k = k % len(linked_list)

    beg = linked_list
    end = linked_list
    for _ in range(k):
        end = end.next

    while end.next:
        beg = beg.next
        end = end.next
    beg_copy = beg

    values_to_shifted = []
    while beg.next:
        beg = beg.next
        values_to_shifted.append(beg)

    initial = linked_list
    while values_to_shifted:
        node = values_to_shifted.pop()
        node.next = initial
        initial = node

    beg_copy.next = None
    return initial


def main():
    linked_list = Node(1, Node(1, Node(2, Node(2, Node(3, Node(5, Node(5, Node(5))))))))
    print("Original: ", linked_list)
    linked_list = remove_duplicates_from_sorted_list(linked_list)
    print(linked_list)

    linked_list2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    print("Shifted Linked List: {}".format(shift_linked_list(linked_list2, 3)))


if __name__ == "__main__":
    main()
