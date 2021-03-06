import math
from typing import List

from linked_list import Node


def is_leaf(node):
    return node is not None and node.left is None and node.right is None


class BST:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                return self.left.insert(value)
            else:
                self.left = BST(value, self)
                return self.left
        else:
            if self.right is not None:
                return self.right.insert(value)
            else:
                self.right = BST(value, self)
                return self.right

    def contains(self, value):
        if value == self.value:
            return self

        if value < self.value:
            if self.left is None:
                return None
            return self.left.contains(value)
        else:
            if self.right is None:
                return None
            return self.right.contains(value)

    def remove(self, value):
        """
		:param value:
		:return: a reference to the new BST without the value
		"""
        node_to_be_removed = self.contains(value)
        if not node_to_be_removed:
            raise ValueError("Value Does not exist in tree")

        if BST._both_children_are_non_null(node_to_be_removed):
            substitute_node = node_to_be_removed._get_substitute_value()
            node_to_be_removed.value = substitute_node.value
            substitute_node.remove(substitute_node.value)
        else:
            child_if_any = node_to_be_removed.left or node_to_be_removed.right

            if not node_to_be_removed.parent:
                assert self is node_to_be_removed
                return child_if_any

            if node_to_be_removed.value < node_to_be_removed.parent.value:
                node_to_be_removed.parent.left = child_if_any
            else:
                node_to_be_removed.parent.right = child_if_any

        return self

    def __repr__(self):
        return "BST(value={})".format(self.value, self.left, self.right)

    @staticmethod
    def _both_children_are_non_null(tree):
        return tree.left is not None and tree.right is not None

    def _get_substitute_value(self):
        substitute_value = self.right

        while substitute_value.left is not None:
            substitute_value = substitute_value.left

        return substitute_value

    def closest_value_to(self, num, current_closest_value=math.inf):
        if abs(num - current_closest_value) >= abs(num - self.value):
            current_closest_value = self.value

        next_node = self.right if num - self.value > 0 else self.left

        if not next_node:
            return current_closest_value
        return next_node.closest_value_to(num, current_closest_value)

    def branch_sums_elegant(self):
        if is_leaf(self):
            return [self.value]

        left_branch_sums = self.left.branch_sums_elegant() if self.left else []
        right_branch_sums = self.right.branch_sums_elegant() if self.right else []

        return list(map(lambda s: s + self.value, left_branch_sums + right_branch_sums))

    def branch_sums(self):
        branches = [{"node": self, "sum": self.value}]

        is_done = False
        while not is_done:
            is_done = True
            subbranches = []

            for branch_index, branch in enumerate(branches):
                if branch["node"].left is None and branch["node"].right is None:
                    subbranches.append(branch)
                    continue

                is_done = False

                items = []

                if branch["node"].left is not None:
                    items.append({"node": branch["node"].left, "sum": branch["sum"] + branch["node"].left.value})
                if branch["node"].right is not None:
                    items.append({"node": branch["node"].right, "sum": branch["sum"] + branch["node"].right.value})

                subbranches.extend(items)

            branches = subbranches

        return map(lambda b: b["sum"], branches)

    def get_node_depths(self):
        def _create_node_info(node, depth):
            return {"node": node, "depth": depth}

        result = {}
        branches = [_create_node_info(self, 0)]

        while branches:
            branch = branches.pop()
            branch_node = branch["node"]
            branch_depth = branch["depth"]
            result[branch_node.value] = branch_depth
            if branch_node.left is not None:
                branches.append(_create_node_info(branch_node.left, branch_depth + 1))
            if branch_node.right is not None:
                branches.append(_create_node_info(branch_node.right, branch_depth + 1))

        return result

    def node_depths_sum(self, depth=0):
        if self.left:
            left_subtree_node_depths_sum = self.left.node_depths_sum(depth=depth + 1)
        else:
            left_subtree_node_depths_sum = 0
        if self.right:
            right_subtree_node_depths_sum = self.right.node_depths_sum(depth=depth + 1)
        else:
            right_subtree_node_depths_sum = 0

        return depth + left_subtree_node_depths_sum + right_subtree_node_depths_sum

    @property
    def depth(self):
        left_depth = self.left.depth if self.left else -1
        right_depth = self.right.depth if self.right else -1

        return 1 + max(left_depth, right_depth)

    @classmethod
    def depth_first_search(cls, tree):
        if tree is None:
            return
        print(tree.value)
        cls.depth_first_search(tree.left)
        cls.depth_first_search(tree.right)

    @classmethod
    def breadth_first_search(cls, tree):
        nodes = [tree]

        while nodes:
            node = nodes.pop(0)
            print(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    @classmethod
    def validate_bst(cls, tree, min_value=-math.inf, max_value=math.inf):
        if tree is None:
            return True

        if not min_value < tree.value < max_value:
            return False

        return cls.validate_bst(tree.left, min_value=min_value, max_value=tree.value) and \
               cls.validate_bst(tree.right, min_value=tree.value, max_value=max_value)

    def in_order_traversal(self):
        result_list = []

        if self.left is not None:
            result_list.extend(self.left.in_order_traversal())

        result_list.append(self.value)

        if self.right is not None:
            result_list.extend(self.right.in_order_traversal())

        return result_list

    def in_order_traversal_iterative_using_stack(self, callback=print):
        visited = set()
        stack = [self]

        result = []

        while stack:
            element = stack[-1]

            if element.left is None or element.left in visited:
                stack.pop()
                result.append(element.value)
                visited.add(element)

                if element.right is not None:
                    stack.append(element.right)
            else:
                stack.append(element.left)

        return result

    def in_order_traversal_iterative(self):
        current_node = self
        prev_node = None

        result = []
        while current_node:
            if current_node.parent is prev_node:
                if current_node.left:
                    next_node = current_node.left
                else:
                    result.append(current_node.value)
                    next_node = current_node.right if current_node.right else current_node.parent
            elif current_node.left == prev_node:
                result.append(current_node.value)
                next_node = current_node.right if current_node.right else current_node.parent
            else:
                next_node = current_node.parent

            prev_node = current_node
            current_node = next_node
        return result

    def pre_order_traversal(self):
        result_list = [self.value]

        if self.left is not None:
            result_list.extend(self.left.pre_order_traversal())

        if self.right is not None:
            result_list.extend(self.right.pre_order_traversal())

        return result_list

    def post_order_traversal(self):
        result_list = []

        if self.left is not None:
            result_list.extend(self.left.post_order_traversal())

        if self.right is not None:
            result_list.extend(self.right.post_order_traversal())

        result_list.append(self.value)

        return result_list

    @classmethod
    def minimum_height_bst(cls, arr, start, end, parent=None):
        if start > end:
            return None

        mid = math.floor((start + end) / 2)
        tree = BST(arr[mid], parent)

        left_subtree = cls.minimum_height_bst(arr, start, mid - 1, tree)
        right_subtree = cls.minimum_height_bst(arr, mid + 1, end, tree)

        tree.left = left_subtree
        tree.right = right_subtree

        return tree

    def get_leaf_nodes(self):
        leaf_nodes = []

        if self.left is not None:
            leaf_nodes.extend([self.left] if is_leaf(self.left) else self.left.get_leaf_nodes())

        if self.right is not None:
            leaf_nodes.extend([self.right] if is_leaf(self.right) else self.right.get_leaf_nodes())

        return leaf_nodes

    def get_all_nodes(self):
        all_nodes = [self]

        if self.left is not None:
            all_nodes.extend(self.left.get_all_nodes())

        if self.right is not None:
            all_nodes.extend(self.right.get_all_nodes())

        return all_nodes

    def reverse_in_order_traversal(self, go_upto=4):
        # Returns BST Elements in Descending order
        result_list = []

        if self.right is not None:
            result_list.extend(self.right.reverse_in_order_traversal(go_upto=go_upto))

        result_list.append(self.value)

        if len(result_list) >= go_upto:
            return result_list[:go_upto]

        if self.left is not None:
            result_list.extend(self.left.reverse_in_order_traversal(go_upto=go_upto - len(result_list)))

        return result_list

    def invert(self):
        if self.left:
            self.left.invert()

        if self.right:
            self.right.invert()

        self.left, self.right = self.right, self.left

    @property
    def height(self):
        return max(BST._height_or_default(self.left), BST._height_or_default(self.right)) + 1

    @staticmethod
    def _height_or_default(tree):
        """
        :param nullable tree:
        :return: height of tree; -1 in case given tree is None
        """
        return tree.height if tree else -1

    def is_balanced(self):
        is_left_tree_balanced = self.left.is_balanced() if self.left else True
        is_right_tree_balanced = self.right.is_balanced() if self.right else True

        return is_left_tree_balanced and is_right_tree_balanced and \
               abs(BST._height_or_default(self.left) - BST._height_or_default(self.right)) <= 1

    def max_path_sum(self):  # Verified on Leetcode
        max_left_sum_branch_including_root, max_left_sum_overall = self.left.max_path_sum() if self.left else (0, 0)
        max_right_sum_branch_including_root, max_right_sum_overall = self.right.max_path_sum() if self.right else (0, 0)

        max_branch_sum_including_root = max(self.value + max_right_sum_branch_including_root,
                                            self.value + max_left_sum_branch_including_root, self.value)
        max_sum_including_root = max(
            max_right_sum_branch_including_root + max_left_sum_branch_including_root + self.value,
            max_branch_sum_including_root)
        max_sum_overall = max(
            [max_sum_including_root] + list(filter(lambda x: x != 0, (max_left_sum_overall, max_right_sum_overall))))

        return max_branch_sum_including_root, max_sum_overall

    @staticmethod
    def get_next_larger_value(tree_node):
        if tree_node.right:
            temp = tree_node.right
            while temp.left is not None:
                temp = temp.left

            return temp
        else:
            temp = tree_node
            while True:
                parent = temp.parent
                if not parent or parent.left == temp:
                    return parent

                temp = temp.parent

    @staticmethod
    def get_next_smaller_value(tree_node):
        if tree_node.left:
            temp = tree_node.left
            while temp.right is not None:
                temp = temp.right

            return temp
        else:
            temp = tree_node
            while True:
                parent = temp.parent
                if not parent or parent.right == temp:
                    return parent

                temp = temp.parent

    def minimum_value(self):
        temp = self
        while temp.left:
            temp = temp.left
        return temp

    def flatten(self):
        temp_value = self.minimum_value()

        start = temp = Node(temp_value)
        while temp:
            temp_value = BST.get_next_larger_value(temp_value)
            temp.next = Node(temp_value.value) if temp_value else None
            temp = temp.next

        return start

    @property
    def diameter(self):
        def get_longest_path_across_tree(node):
            queue = [[node]]
            seen = set()
            diameter = -1

            while queue:
                diameter += 1

                temp = []
                for node in queue.pop():
                    seen.add(node)

                    if node.parent is not None and node.parent not in seen:
                        temp.append(node.parent)
                    if node.left is not None and node.left not in seen:
                        temp.append(node.left)
                    if node.right is not None and node.right not in seen:
                        temp.append(node.right)

                if temp:
                    queue.append(temp)

            return diameter

        return max(map(get_longest_path_across_tree, self.get_leaf_nodes()))

    def get_diameter(self):  # Verified on Leetcode
        left_diameter, longest_branch_length_left_subtree = self.left.get_diameter() if self.left else (0, -1)
        right_diameter, longest_branch_length_right_subtree = self.right.get_diameter() if self.right else (0, -1)

        potential_diameter = 2 + longest_branch_length_left_subtree + longest_branch_length_right_subtree
        diameter = max(left_diameter, right_diameter, potential_diameter)
        longest_branch = 1 + max(longest_branch_length_left_subtree, longest_branch_length_right_subtree)

        return diameter, longest_branch


def reconstruct_bst_from_preorder_traversal(arr, parent=None):  # Accepted on LeetCode
    if not arr:
        return None

    tree = BST(arr[0], parent)
    right_subtree_starts_at = None
    for i in range(1, len(arr)):
        if arr[i] >= arr[0]:
            right_subtree_starts_at = i
            break

    tree.left = reconstruct_bst_from_preorder_traversal(arr[1: right_subtree_starts_at], tree)
    if right_subtree_starts_at is not None:
        tree.right = reconstruct_bst_from_preorder_traversal((arr[right_subtree_starts_at:]))

    return tree


def find_successor(tree, node):
    assert node is not None

    temp = node.right
    if temp is not None:
        while temp.left is not None:
            temp = temp.left

        return temp

    while node.parent is not None:
        if node.parent.left == node:
            return node.parent

        node = node.parent

    return -1


def parent_chain(node):
    while node:
        yield node
        node = node.parent


def youngest_common_ancestor(node1, node2):
    chain1 = reversed(list(parent_chain(node1)))
    chain2 = reversed(list(parent_chain(node2)))

    common_ancestor = None
    while True:
        parent1 = next(chain1, None)
        parent2 = next(chain2, None)

        if parent1 is None or parent2 is None or parent1 != parent2:
            break
        common_ancestor = parent1

    return common_ancestor


def is_same_bst(bst1: List, bst2: List):
    def _get_left_and_right_subtrees(tree):
        left_tree = []
        right_tree = []

        for index in range(1, len(tree)):
            if tree[index] <= tree[0]:
                left_tree.append(tree[index])
            else:
                right_tree.append(tree[index])

        return left_tree, right_tree

    if len(bst1) != len(bst2):
        return False
    if len(bst1) == 0:
        return True

    left_subtree_original, right_subtree_original = _get_left_and_right_subtrees(bst1)
    left_subtree, right_subtree = _get_left_and_right_subtrees(bst2)

    return bst1[0] == bst2[0] and is_same_bst(left_subtree_original, left_subtree) and is_same_bst(
        right_subtree_original, right_subtree)


def find_nodes_k_distance(tree_node, k, visited):
    result = []

    if not tree_node or tree_node in visited:
        return result

    if k == 0:
        return [tree_node.value]

    visited.add(tree_node)

    result.extend(find_nodes_k_distance(tree_node.parent, k - 1, visited))
    result.extend(find_nodes_k_distance(tree_node.left, k - 1, visited))
    result.extend(find_nodes_k_distance(tree_node.right, k - 1, visited))

    return result


def node_depths_recursive(tree):
    """
    :param tree: BST
    :return: Sum of Depths of All Nodes in Tree and no. of nodes
    """

    if not tree:
        return 0, 0

    if is_leaf(tree):
        return 0, 1

    node_depths_left, count_of_nodes_left = node_depths_recursive(tree.left)
    node_depths_right, count_of_nodes_right = node_depths_recursive(tree.right)

    node_depths = node_depths_left + count_of_nodes_left + node_depths_right + count_of_nodes_right
    return node_depths, count_of_nodes_right + count_of_nodes_left + 1


def flatten_binary_tree_recursive(tree):
    if not tree.left:
        left_most = tree
    else:
        flattened_left_tree_head, flattened_left_tree_tail = flatten_binary_tree_recursive(tree.left)
        flattened_left_tree_tail.right = tree
        tree.left = flattened_left_tree_tail
        left_most = flattened_left_tree_head

    if not tree.right:
        right_most = tree
    else:
        flattened_right_tree_head, flattened_right_tree_tail = flatten_binary_tree_recursive(tree.right)
        tree.right = flattened_right_tree_head
        flattened_right_tree_head.left = tree
        right_most = flattened_right_tree_tail

    return left_most, right_most


def flatten_tree(root):
    flattened_tree = flatten_binary_tree_recursive(root)[0]
    result = []
    while flattened_tree:
        result.append(flattened_tree.value)
        flattened_tree = flattened_tree.right
    return result


def number_of_binary_tree_topologies(num):
    if num == 0:
        return 1
    number_of_topologies = 0
    left_subtree_size = 0
    while left_subtree_size <= num - 1:
        left_subtree_topologies = number_of_binary_tree_topologies(left_subtree_size)
        right_subtree_topologies = number_of_binary_tree_topologies(num - 1 - left_subtree_size)
        number_of_topologies += left_subtree_topologies * right_subtree_topologies
        left_subtree_size += 1

    return number_of_topologies

def main():
    tree = create_bst_tree1()
    tree2 = create_bst_tree2()
    print("Find Closest Value in BST: {}".format(tree.closest_value_to(8.8)))
    invalid_bst = BST(6, None, BST(3, None), BST)

    res = list(tree.branch_sums())
    print("Branch Sums: {}".format(res))
    print("Branch Sums Elegant: {}".format(tree.branch_sums_elegant()))
    print("Binary Tree Diameter {}".format(tree.get_diameter()))
    result = tree.get_node_depths()
    print("Node Depths: {}".format(tree.node_depths_sum()))
    print("Pre Order Traversal: {}".format(tree.pre_order_traversal()))
    print("Post-Order Traversal: {}".format(tree.post_order_traversal()))
    # BST.depth_first_search(tree)
    sorted_arr = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    # min_height_tree = BST.minimum_height_bst(sorted_arr, 0, len(sorted_arr) - 1)
    print("Kth Largest Value : {}".format(tree.reverse_in_order_traversal(go_upto=3)))
    # tree.in_order_traversal_iterative()
    # pre_order_bst_as_array = [10, 4, 2, 1, 5, 5, 17, 19, 18]
    # new_tree = reconstruct_bst_from_preorder_traversal(pre_order_bst_as_array)

    # leaf_nodes = tree.get_leaf_nodes()
    print("In-Order Traversal: {}".format(tree.in_order_traversal_iterative_using_stack()))

    node_ref_1 = tree.insert(45)
    node_ref_2 = tree.insert(15.5)
    print("Youngest Common Ancestor: {}".format(youngest_common_ancestor(node_ref_1, node_ref_2)))
    print("Is Same BST: {}".format(is_same_bst([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81])))

    print("Max Path Sum: {}".format(BST(-3, None).max_path_sum()))

    node_ref_3 = tree.insert(12.5)
    print("Find Nodes K-distance: {}".format(find_nodes_k_distance(node_ref_3, 4, visited=set())))
    print("Next Larger Value: {}".format(BST.get_next_larger_value(node_ref_3)))
    print("Flatten Tree: {}".format(tree.flatten()))
    # print("Flatten Binary Tree Recursive: {}".format(flatten_tree(tree)))
    print("Depth: {}".format(tree.depth))
    print("Number of Binary Tree Topologies: {}".format(number_of_binary_tree_topologies(3)))


def create_bst_tree1():
    """
		   13
		 /	  \
		9	   16
	  /   \   /  \
	 5    10 14   22
    / \     \  \    \
   2   6    11 15   23
  /      \    \
-1        7   12
           \
            8
	"""
    tree = BST(13, None)
    tree.insert(9)
    tree.insert(16)
    tree.insert(5)
    tree.insert(10)
    tree.insert(14)
    tree.insert(22)
    tree.insert(2)
    tree.insert(6)
    tree.insert(11)
    tree.insert(15)
    tree.insert(23)
    tree.insert(-1)
    tree.insert(7)
    tree.insert(12)
    tree.insert(8)
    return tree


def create_bst_tree2():
    """
        15
       /  \
      10  17
     / \
    8  12
   /    \
  6     13
 /       \
4        14
    """
    tree = BST(15, None)
    tree.insert(10)
    tree.insert(17)
    tree.insert(8)
    tree.insert(12)
    tree.insert(6)
    tree.insert(13)
    tree.insert(4)
    tree.insert(14)

    return tree


if __name__ == '__main__':
    main()
