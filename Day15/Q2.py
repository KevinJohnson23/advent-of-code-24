from PerformanceTester.PerformanceTester import test_time

directions_map = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

def get_box_intervals(grid, x, y, dx, dy, seen=None):
    if seen is None:
        seen = set()
    seen.add((x, y))

    box_intervals = set()

    box_start_x, box_start_y = x, y
    box_end_x, box_end_y = box_start_x, box_start_y

    while True:
        next_box_x, next_box_y = box_end_x + dx, box_end_y + dy
        if grid[next_box_y][next_box_x] == "#":
            box_start_x = None
            break
        elif grid[next_box_y][next_box_x] in "[]":
            box_end_x, box_end_y = next_box_x, next_box_y
            seen.add((box_end_x, box_end_y))
        else:
            break

    if box_start_x is None:
        return
    box_intervals.add(((box_start_x, box_start_y), (box_end_x, box_end_y)))

    if dx == 0:
        if grid[y][x] == "[":
            if (x+1, y) not in seen:
                right_box_intervals = get_box_intervals(grid, x + 1, y, dx, dy, seen)
                if not right_box_intervals:
                    return
                box_intervals = box_intervals.union(right_box_intervals)
        else:
            if (x-1, y) not in seen:
                left_box_intervals = get_box_intervals(grid, x - 1, y, dx, dy, seen)
                if not left_box_intervals:
                    return
                box_intervals = box_intervals.union(left_box_intervals)

        for interval_start, interval_end in box_intervals:
            start_x, start_y = interval_start
            end_x, end_y = interval_end

            for box_y in range(start_y, end_y+dy, dy):
                if grid[box_y][start_x] == "[":
                    if (start_x+1, box_y) not in seen:
                        right_box_intervals = get_box_intervals(grid, start_x + 1, box_y, dx, dy, seen)
                        if not right_box_intervals:
                            return
                        box_intervals = box_intervals.union(right_box_intervals)
                else:
                    if (start_x-1, box_y) not in seen:
                        left_box_intervals = get_box_intervals(grid, start_x - 1, box_y, dx, dy, seen)
                        if not left_box_intervals:
                            return
                        box_intervals = box_intervals.union(left_box_intervals)

    return box_intervals

def main():
    with open("input.txt") as file:
        file_content = file.read()
    grid, directions = file_content.split("\n\n")

    grid = [list(row) for row in grid.split("\n")]
    h, w = len(grid), len(grid[0])

    directions = directions.replace("\n", "")

    current_x, current_y = None, None
    wide_grid = []
    for y in range(h):
        row = grid[y]
        wide_row = []
        for cell in row:
            if cell == "@":
                current_x, current_y = len(wide_row), y
                wide_row.extend(["@", "."])
            elif cell == "O":
                wide_row.extend(["[", "]"])
            else:
                wide_row.extend([cell]*2)
        wide_grid.append(wide_row)


    for direction in directions:
        dx, dy = directions_map[direction]
        new_x, new_y = current_x + dx, current_y + dy

        if wide_grid[new_y][new_x] == "#":
            continue

        if wide_grid[new_y][new_x] in "[]":
            box_intervals = get_box_intervals(wide_grid, new_x, new_y, dx, dy)
            if box_intervals is None:
                continue

            for interval_start, interval_end in box_intervals:
                start_x, start_y = interval_start
                end_x, end_y = interval_end

                y_iterator = -dy if dy else 1
                x_iterator = -dx if dx else 1
                for box_y in range(end_y, start_y+y_iterator, y_iterator):
                    for box_x in range(end_x, start_x+x_iterator, x_iterator):
                        wide_grid[box_y+dy][box_x+dx] = wide_grid[box_y][box_x]
                        wide_grid[box_y][box_x] = "."

        wide_grid[current_y][current_x] = "."
        current_x, current_y = new_x, new_y
        wide_grid[current_y][current_x] = "@"

    gps = 0
    for y in range(len(wide_grid)):
        for x in range(len(wide_grid[0])):
            if wide_grid[y][x] == "[":
                gps += y * 100 + x
    print(gps)

if __name__ == "__main__":
    test_time(main)