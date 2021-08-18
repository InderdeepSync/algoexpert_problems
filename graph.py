

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

def dijkstra_algorithm(graph, start_node):
    def _get_next_min_distance_vertex():
        node = None
        min_distance = float("inf")
        for index in range(len(min_distances)):
            if index in visited:
                continue

            if min_distance >= min_distances[index]:
                node = index
                min_distance = min_distances[index]
        return node, min_distance

    min_distances = [float("inf") for _ in graph]
    min_distances[start_node] = 0

    visited = set()
    while len(visited) != len(graph):
        node, min_distance = _get_next_min_distance_vertex()

        if min_distance == float("inf"):
            break

        visited.add(node)

        for child_node, edge_weight in graph[node]:
            if child_node in visited:
                continue

            min_distances[child_node] = min(min_distances[child_node], min_distance + edge_weight)

    return min_distances


def topological_sort_kahn(graph):
    in_degree = [0 for _ in graph]
    for index in range(len(graph)):
        for child in graph[index]:
            in_degree[child] = in_degree[child] + 1

    queue = []
    for index in range(len(in_degree)):
        if in_degree[index] == 0:
            queue.append(index)

    result = []
    visited = set()
    while queue:
        node = queue.pop(0)
        result.append(node)
        visited.add(node)

        for child in graph[node]:
            in_degree[child] = in_degree[child] - 1
            if in_degree[child] == 0:
                queue.append(child)

    if len(visited) != len(graph):
        raise ValueError("Topological Sort Not Possible")

    return result

def topological_sort(graph):
    def _dfs(vertex):
        visited.add(vertex)

        for child in filter(lambda c: c not in visited, graph[vertex]):
            _dfs(child)

        stack.append(vertex)

    stack = []
    visited = set()
    for vertice in range(len(graph)):
        if vertice in visited:
            continue
        _dfs(vertice)

    stack.reverse()
    return stack



if __name__ == "__main__":
    print(number_of_ways_to_traverse_graph(3, 4))

    graph1 = [[1, 3], [2, 3, 4], [], [], [2, 5], []]
    graph2 = [[1, 2], [3], [3], []]
    print("Does graph have any cycles: {}".format(cycle_in_graph(graph2)))
    print("Depth First Search: {}".format(depth_first_traversal(graph2, 0, set())))

    graph3 = [[], [], [3], [1], [0, 1], [0, 2]]
    weighted_graph = [[(1, 7)], [(2, 6), (3, 20), (4, 3)], [(3, 14)], [(4, 2)], [], []]
    print("Dijkstra's Algorithm: {}".format(dijkstra_algorithm(weighted_graph, 0)))
    print("Topological Sort(Kahn): {}".format(topological_sort_kahn(graph1)))
    print("Topological Sort: {}".format(topological_sort(graph3)))