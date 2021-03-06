from itertools import groupby
from pprint import pprint as pp

def convert_into_edges_map(points):
    get_x_coordinate = lambda point: point[0]
    points.sort(key=get_x_coordinate)

    edges_map = {}
    for key, items in groupby(points, get_x_coordinate):
        prev_items = []
        for item in sorted(items, key=lambda point: point[1]):
            for prev_item in prev_items:
                edge = (prev_item[1], item[1])
                edges_map.setdefault(edge, []).append(key)

            prev_items.append(item)

    return edges_map

def minimum_area_rectangle(points):  # Accepted on Leetcode
    edges_map = convert_into_edges_map(points)

    min_area = float('inf')
    for edge, x_coordinates in edges_map.items():
        prev_coordinate = None
        min_breadth = float('inf')
        for coordinate in x_coordinates:
            if prev_coordinate is None:
                prev_coordinate = coordinate
                continue
            min_breadth = min(min_breadth, coordinate - prev_coordinate)
            prev_coordinate = coordinate

        edge_length = edge[1] - edge[0]
        min_area = min(min_area, edge_length * min_breadth)

    return min_area


def rectangle_mania(points):
    edges_map = convert_into_edges_map(points)

    no_of_rectangles = 0
    for edge, x_coordinates in edges_map.items():
        no_of_rectangles += len(x_coordinates) * (len(x_coordinates) - 1)//2

    return no_of_rectangles


if __name__ == "__main__":
    input_points = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
    pp("Minimum Area Rectangle: {}".format(
        minimum_area_rectangle(input_points)))

    print("Rectangle Mania: {}".format(rectangle_mania(input_points)))
