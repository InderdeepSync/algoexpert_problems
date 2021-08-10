class Node:
    def __init__(self, value, nexxt=None):
        self.value = value
        self.next = nexxt

    def __repr__(self):
        return "Node(value={}, next={})".format(self.value, self.next)

    def __str__(self):
        return repr(self)


def remove_duplicates_from_sorted_list(linked_list):
    initial = linked_list

    last_encountered = linked_list.value
    parent = linked_list
    linked_list = linked_list.next

    while linked_list:
        if linked_list.value == last_encountered:
            temp = linked_list

            parent.next = linked_list.next
            linked_list = linked_list.next

            temp.next = None
            continue

        last_encountered = linked_list.value
        parent = linked_list
        linked_list = linked_list.next

    return initial


def main():
    linked_list = Node(1, Node(1, Node(2, Node(2, Node(3, Node(5, Node(5, Node(5))))))))
    print("Original: ", linked_list)
    linked_list = remove_duplicates_from_sorted_list(linked_list)
    print(linked_list)


if __name__ == "__main__":
    main()
