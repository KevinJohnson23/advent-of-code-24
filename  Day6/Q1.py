from PerformanceTester.PerformanceTester import test_time

obs = {"^":0,
       ">":1,
       "v":2,
       "<":3}
dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def has_obstacle(path, x, y, w, h):
    if x in [-1, w] or y in [-1, h]:
        return False
    return path[y][x] == "#"

def get_distinct(path, current_x, current_y, current_idx, w, h):
    distinct = dict()
    while True:
        if current_x in [-1, w] or current_y in [-1, h]:
            break
        distinct[current_x, current_y] = 1

        while has_obstacle(path, current_x + dirs[current_idx][0], current_y + dirs[current_idx][1], w, h):
            current_idx = (current_idx + 1) % 4
        current_y += dirs[current_idx][1]
        current_x += dirs[current_idx][0]

    return len(distinct.keys())

def main():
    with open("input.txt") as file:
        lines = file.readlines()
        h = len(lines)
        w = len(lines[0])
        for y in range(h):
            for x in range(w):
                if lines[y][x] in "^<>v":
                    start_x = x
                    start_y = y
                    start_idx = obs[lines[y][x]]
                    print(get_distinct(lines, start_x, start_y, start_idx, w, h))
                    return

if __name__ == "__main__":
    test_time(main)
