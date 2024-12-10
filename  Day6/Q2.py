from PerformanceTester.PerformanceTester import test_time

obs = {"^": 0,
       ">": 1,
       "v": 2,
       "<": 3}
dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def is_outside(x, y, w, h):
    return x < 0 or y < 0 or x >= w or y >= h


def is_blocked(graph, x, y, dir, w, h):
    x += dir[0]
    y += dir[1]
    return not is_outside(x, y, w, h) and graph[y][x] == "#"

def has_obstacle(path, x, y, w, h):
    if x in [-1, w] or y in [-1, h]:
        return False
    return path[y][x] == "#"

def copy_visited(visited):
    visited_copy = set()
    for visited_node in visited:
        visited_copy.add((visited_node[0], visited_node[1], visited_node[2]))
    return visited_copy

def get_loops(graph, x, y, index, w, h, visited, recurse=False):
    loops = 0
    while True:
        while has_obstacle(graph, x + dirs[index][0], y + dirs[index][1], w, h):
            index = (index + 1) % 4

        new_x = x + dirs[index][0]
        new_y = y + dirs[index][1]

        if new_x in [-1, w] or new_y in [-1, h]:
            return loops, False

        if recurse:
            graph[new_y] = graph[new_y][:new_x] + "#" + graph[new_y][new_x + 1:]
            _, looped = get_loops(graph, x, y, index, w, h, copy_visited(visited))
            graph[new_y] = graph[new_y][:new_x] + "." + graph[new_y][new_x + 1:]
            if looped:
                loops += 1
        elif (new_x, new_y, index) in visited:
                return None, True
        visited.add((new_x, new_y, index))

        x, y = new_x, new_y

def main():
    with open("input.txt") as file:
        lines = file.readlines()
        h = len(lines)
        w = len(lines[0])
        for y in range(h):
            for x in range(w):
                if lines[y][x] in "^<>v":
                    start_idx = obs[lines[y][x]]
                    print(get_loops(lines, x, y, obs[lines[y][x]], w, h, {(x, y, start_idx)},True)[0])
                    return

if __name__ == "__main__":
    test_time(main)
