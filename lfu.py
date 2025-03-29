
class Node:
    def __init__(self, value, list_pointer=None, prev=None, nnext=None):
        self.value = value
        self.list_p =  list_pointer
        self.prev = prev
        self.next = nnext


class LFUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.freq_list = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        value_node = self.map[key]
        freq_node =  self.map[key].list_p

        if not freq_node.next:
            freq_node.next = Node(freq_node.value + 1)
            freq_node.next.prev = freq_node
        elif freq_node.next.value != freq_node.value + 1:
            new_node = Node(freq_node.value + 1, None, freq_node, freq_node.next)
            freq_node.next.prev = new_node
            freq_node.next = new_node

        if value_node.prev:
            value_node.prev.next = value_node.next

        if value_node.next:
            value_node.next.prev = value_node.prev

        if freq_node.list_p is value_node:
            freq_node.list_p = value_node.next
            if freq_node.list_p is None:
                self._remove_from_freq_list(freq_node)

        value_node.prev = None
        value_node.next = freq_node.next.list_p
        if value_node.next:
            value_node.next.prev = value_node
        value_node.list_p = freq_node.next
        freq_node.next.list_p = value_node

        return value_node.value[1]


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            _ = self.get(key)
            self.map[key].value = (key, value)
            return

        if len(self.map) == self.capacity:
            # Eviction here: remove element of the least freq that was used least recently
            temp = self.freq_list
            while temp.list_p is None:
                temp = temp.next

            temp2 = temp
            temp = temp.list_p
            while temp.next is not None:
                temp = temp.next

            delete_key, _  = temp.value
            if temp.prev:
                temp.prev.next = None
            else:
                temp2.list_p = None
                self._remove_from_freq_list(temp2)

            del self.map[delete_key]

        if not self.freq_list:
            self.freq_list = Node(1)

        if self.freq_list.value != 1:
            f_node = Node(1)
            f_node.next = self.freq_list
            f_node.next.prev = f_node
            self.freq_list = f_node

        node = Node((key, value), self.freq_list)
        if self.freq_list.list_p:
            node.next = self.freq_list.list_p
            node.next.prev = node
        self.freq_list.list_p = node

        self.map[key] = node

    def _remove_from_freq_list(self, freq_node):
        if freq_node.prev is not None:
            freq_node.prev.next = freq_node.next
        else:
            self.freq_list = freq_node.next

        if freq_node.next is not None:
            freq_node.next.prev = freq_node.prev





if __name__ == "__main__":
    cache = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    print(cache.get(2))