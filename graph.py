

class Graph:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Graph(name))


def number_of_ways_to_traverse_graph(height, width):
    if height == 1 or width == 1:
        return 1

    return number_of_ways_to_traverse_graph(height - 1, width) + number_of_ways_to_traverse_graph(height, width - 1)

def depth_first_traversal(adjacency_matrix, vertice, visited):
    assert 0 <= vertice <= len(adjacency_matrix) - 1

    visited.add(vertice)

    res = [vertice]
    for child in filter(lambda c: c not in visited, adjacency_matrix[vertice]):
        res.extend(depth_first_traversal(adjacency_matrix, child, visited))

    return res

def breadth_first_traversal(adjacency_matrix, vertice):
    assert 0 <= vertice <= len(adjacency_matrix) - 1

    visited = set()
    res = []

    under_processing = [vertice]

    while under_processing:
        cur = under_processing.pop(0)
        visited.add(cur)
        res.append(cur)

        under_processing.extend(filter(lambda c: c not in visited, adjacency_matrix[cur]))

    return res


def cycle_in_graph(adjacency_matrix): # Accepted on LeetCode
    vertices = set(range(len(adjacency_matrix)))

    def _depth_first_traversal(vertex, visited):
        if vertex in visited:
            return True

        visited.add(vertex)

        for child in adjacency_matrix[vertex]:
            if _depth_first_traversal(child, set(visited)):
                return True

        return False

    for vertice in vertices:
        if _depth_first_traversal(vertice, set()):
            return True

    return False



if __name__ == "__main__":
    print(number_of_ways_to_traverse_graph(3, 4))

    graph1 = [[1, 3], [2, 3, 4], [ ], [], [2, 5], []]
    graph2 = [[1, 2], [3], [3], []]
    print("Does graph have any cycles: {}".format(cycle_in_graph(graph2)))