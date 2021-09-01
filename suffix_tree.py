

class SuffixTree:
    def __init__(self, char, children):
        self.char = char
        self.children = children

    def __repr__(self):
        return "SuffixTree(char={})".format(self.char)

    def contains(self, string):
        temp_index = 0
        sub_tree = self

        while temp_index < len(string):
            new_sub_tree = sub_tree.get_child_with_char(string[temp_index])
            if not new_sub_tree:
                return False

            temp_index += 1
            sub_tree = new_sub_tree

        return SuffixTree.has_char_in_children(sub_tree, "*")


    @classmethod
    def create_suffix_tree_from(cls, string):
        tree = cls(char="/", children=[])

        for index in range(len(string)):
            suffix = string[index:]
            tree.add_suffix_to_tree(suffix)

        return tree

    def add_suffix_to_tree(self, suffix):
        temp_index = 0
        sub_tree = self
        while temp_index < len(suffix):
            new_sub_tree = sub_tree.get_child_with_char(suffix[temp_index])
            if not new_sub_tree:
                break

            sub_tree = new_sub_tree
            temp_index += 1

        sub_tree.children.append(SuffixTree._convert_string_to_tree(suffix, temp_index))


    @staticmethod
    def has_char_in_children(tree_node, char):
        return any(node.char == char for node in tree_node.children)

    @classmethod
    def _convert_string_to_tree(cls, string, start_index):
        if start_index == len(string):
            terminator_node = SuffixTree("*", None)
            terminator_node.word_formed = string
            return terminator_node
        return SuffixTree(string[start_index], [cls._convert_string_to_tree(string, start_index + 1)])

    def get_child_with_char(self, char):
        temp = None
        for child in self.children:
            if child.char == char:
                temp = child
                break

        return temp


if __name__ == "__main__":
    suffix_tree = SuffixTree.create_suffix_tree_from("babacad")
    suffix_tree.add_suffix_to_tree("baby")
    suffix_tree.add_suffix_to_tree("babacad")
    print(suffix_tree.contains("babacad"))