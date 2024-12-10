from PerformanceTester.PerformanceTester import test_time

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def copy_graph(graph):
    graph_copy = []
    for row in graph:
        graph_copy.append(row.copy())
    return graph_copy


def copy_visited(visited):
    visited_copy = dict()
    for x, y in visited:
        visited_copy[x, y] = (visited[x, y][0], visited[x, y][1])
    return visited_copy


def is_outside(x, y, w, h):
    return x < 0 or y < 0 or x >= w or y >= h


def is_blocked(graph, x, y, dir, w, h):
    x += dir[0]
    y += dir[1]
    return not is_outside(x, y, w, h) and graph[y][x] == "#"


def copy_dict(d):
    copy = dict()
    for key in d.keys():
        copy[key] = d[key].copy()
    return copy


def traverse(graph, start_x, start_y, w, h, index):
    x, y = start_x, start_y
    visited = dict()

    while True:
        while is_blocked(graph, x, y, directions[index], w, h):
            index = (index + 1) % len(directions)

        new_x = x + directions[index][0]
        new_y = y + directions[index][1]

        if is_outside(new_x, new_y, w, h):
            return visited

        if (new_x, new_y) not in visited:
            visited[new_x, new_y] = (
                (x, y),
                index
            )
        elif index == visited[new_x, new_y][1]:
            return False

        x, y = new_x, new_y


def get_loops(graph, start_x, start_y, w, h, index=0):
    visited_nodes = traverse(graph, start_x, start_y, w, h, index)

    loops = 0

    for x, y in visited_nodes:
        if x == start_x and y == start_y:
            continue

        graph_copy = copy_graph(graph)
        graph_copy[y][x] = "#"

        visited_entry = visited_nodes[x, y][0]
        visited_index = visited_nodes[x, y][1]

        if not traverse(graph_copy, visited_entry[0], visited_entry[1], w, h, visited_index):
            loops += 1

    return loops


def main():
    with open("input.txt") as file:
        start_x = 0
        start_y = 0

        lines = file.readlines()
        h = len(lines)
        w = 0

        for y in range(h):
            lines[y] = list(lines[y].replace("\n", ""))
            if w == 0:
                w = len(lines[y])
            for x in range(w):
                if lines[y][x] in "^<>v":
                    start_x = x
                    start_y = y

        print(get_loops(lines, start_x, start_y, w, h))


if __name__ == "__main__":
    test_time(main)
