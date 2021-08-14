

class SuffixTree:
    def __init__(self, char, children):
        self.char = char
        self.children = children

    def __repr__(self):
        return "SuffixTree(char={})".format(self.char)

    @classmethod
    def create_suffix_tree_from(cls, string):
        tree = cls(char="/", children=[])

        for index in range(len(string)):
            suffix = string[index:]
            tree.add_suffix_to_tree(suffix)

        return tree

    def add_suffix_to_tree(self, suffix):
        sub_tree = self.get_child_with_char(suffix[0])

        if not sub_tree:
            self.children.append(SuffixTree._convert_string_to_tree(suffix))
        else:
            tree2 = self
            for index_char, char in enumerate(suffix):
                sub_tree = tree2.get_child_with_char(char)

                if sub_tree is None:
                    tree2.children.append(SuffixTree._convert_string_to_tree(suffix[index_char:]))
                    break
                else:
                    tree2 = sub_tree

    @staticmethod
    def _has_char_in_children(tree_node, char):
        return any(node.char == char for node in tree_node.children)

    @classmethod
    def _convert_string_to_tree(cls, string):
        if not string:
            return SuffixTree("*", None)
        return SuffixTree(string[0], [cls._convert_string_to_tree(string[1:])])

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
    print(suffix_tree)