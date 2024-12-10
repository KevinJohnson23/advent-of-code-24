from PerformanceTester.PerformanceTester import test_time

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

def has_obstacle(path, x, y, w, h):
    if x in [-1, w] or y in [-1, h]:
        return False
    return path[y][x] == "#"

def traverse(graph, x, y, w, h, index):
    visited = dict()

    while True:
        while has_obstacle(graph, x + dirs[index][0], y + dirs[index][1], w, h):
            index = (index + 1) % 4

        new_x = x + dirs[index][0]
        new_y = y + dirs[index][1]

        if new_x in [-1, w] or new_y in [-1, h]:
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

        graph[y][x] = "#"

        visited_entry = visited_nodes[x, y][0]
        visited_index = visited_nodes[x, y][1]

        if not traverse(graph, visited_entry[0], visited_entry[1], w, h, visited_index):
            loops += 1

        graph[y][x] = "."
    return loops

def main():
    lines = None
    with open("input.txt") as file:
        lines = [list(line.strip()) for line in file]
    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        for x in range(w):
            if lines[y][x] in "^<>v":
                print(get_loops(lines, x, y, w, h))
                return

if __name__ == "__main__":
    test_time(main)
