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


def rearrange_linked_list(list1, k):
    current = list1
    less_start = less_than_k = Node("/")
    more_start = more_than_k = Node("/")
    equal_start = equal_to_k = Node("/")
    while current:
        temp_next = current.next
        current.next = None

        if current.value == k:
            equal_to_k.next = current
            equal_to_k = current
        elif current.value < k:
            less_than_k.next = current
            less_than_k = current
        else:
            more_than_k.next = current
            more_than_k = current

        current = temp_next

    equal_to_k.next = more_start.next
    less_than_k.next = equal_start.next

    return less_start.next


def _split_linked_list(linked_list):
    slow = fast = linked_list

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    second_list = slow.next
    slow.next = None
    return linked_list, second_list

def zip_linked_list(list1):
    list1, list2 = _split_linked_list(list1)
    list2 = reverse_linked_list(list2) if list2 else None

    result_list = temp = Node("/")
    while True:
        if not list1:
            break
        temp.next = list1
        list1 = list1.next
        temp = temp.next

        if not list2:
            continue

        temp.next = list2
        list2 = list2.next
        temp = temp.next

    return result_list.next


def linked_list_palindrome(linked_list):
    list1, list2 = _split_linked_list(linked_list)
    list2 = reverse_linked_list(list2) if list2 else None

    while True:
        if not list2:
            return True

        if list1.value != list2.value:
            return False

        list1 = list1.next
        list2 = list2.next


def main():
    linked_list = Node(1, Node(1, Node(2, Node(2, Node(3, Node(5, Node(5, Node(5))))))))
    print("Original: ", linked_list)
    linked_list = remove_duplicates_from_sorted_list(linked_list)
    print(linked_list)

    linked_list2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
    # print("Shifted Linked List: {}".format(shift_linked_list(linked_list2, 3)))
    # print("Reverse Linked List: {}".format(reverse_linked_list(linked_list2)))

    linked_list3 = Node(2, Node(6, Node(7, Node(8))))
    linked_list4 = Node(1, Node(3, Node(4, Node(4, Node(3, Node(1))))))
    # print("Merge Sorted Linked Lists: {}".format(merge_linked_lists(linked_list3, linked_list4)))

    linked_list5 = Node(3, Node(0, Node(5, Node(3, Node(2, Node(1, Node(4, Node(-1))))))))
    print("Rearrange Linked List: {}".format(rearrange_linked_list(linked_list5, 2.5)))

    print("Zip Linked List: {}".format(zip_linked_list(linked_list2)))
    print("Linked List Palindrome: {}".format(linked_list_palindrome(linked_list4)))


if __name__ == "__main__":
    main()
