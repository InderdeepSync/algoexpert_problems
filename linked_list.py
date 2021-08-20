import math


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

    initial = linked_list
    temp = beg.next
    beg.next = None
    while temp:
        temp2 = temp.next
        temp.next = initial
        initial = temp
        temp = temp2

    return initial

def reverse_linked_list(linked_list):
    prev = linked_list
    current = linked_list.next
    linked_list.next = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev

def merge_linked_lists(list1, list2):
    result_list = temp = Node("/")
    while list1 and list2:
        if list1.value < list2.value:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next

    while list1:
        temp.next = list1
        temp = temp.next
        list1 = list1.next

    while list2:
        temp.next = list2
        temp = temp.next
        list2 = list2.next

    return result_list.next

def main():
    linked_list = Node(1, Node(1, Node(2, Node(2, Node(3, Node(5, Node(5, Node(5))))))))
    print("Original: ", linked_list)
    linked_list = remove_duplicates_from_sorted_list(linked_list)
    print(linked_list)

    linked_list2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    print("Shifted Linked List: {}".format(shift_linked_list(linked_list2, 3)))
    print("Reverse Linked List: {}".format(reverse_linked_list(linked_list2)))

    linked_list3 = Node(2, Node(6, Node(7, Node(8))))
    linked_list4 = Node(1, Node(3, Node(4, Node(5, Node(9, Node(10))))))
    print("Merge Sorted Linked Lists: {}".format(merge_linked_lists(linked_list3, linked_list4)))


if __name__ == "__main__":
    main()
