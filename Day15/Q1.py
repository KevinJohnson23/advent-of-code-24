from PerformanceTester.PerformanceTester import test_time

directions_map = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

def main():
    with open("input.txt") as file:
        file_content = file.read()
    grid, directions = file_content.split("\n\n")

    grid = [list(row) for row in grid.split("\n")]
    h, w = len(grid), len(grid[0])

    directions = directions.replace("\n", "")

    current_x, current_y = None, None
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "@":
                current_x, current_y = x, y
                break
        if current_x:
            break

    for direction in directions:
        dx, dy = directions_map[direction]
        new_x, new_y = current_x + dx, current_y + dy

        if grid[new_y][new_x] == "#":
            continue

        if grid[new_y][new_x] == "O":
            box_start_x, box_start_y = new_x, new_y
            box_end_x, box_end_y = box_start_x, box_start_y

            while True:
                next_box_x, next_box_y = box_end_x + dx, box_end_y + dy
                if grid[next_box_y][next_box_x] == "#":
                    box_start_x = None
                    break
                elif grid[next_box_y][next_box_x] == "O":
                    box_end_x, box_end_y = next_box_x, next_box_y
                else:
                    break

            if box_start_x is None:
                continue

            while True:
                grid[box_end_y+dy][box_end_x+dx] = grid[box_end_y][box_end_x]

                if box_end_x == box_start_x and box_end_y == box_start_y:
                    break

                box_end_x -= dx
                box_end_y -= dy

        grid[current_y][current_x] = "."
        current_x, current_y = new_x, new_y
        grid[current_y][current_x] = "@"

    gps = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O":
                gps += y * 100 + x
    print(gps)

if __name__ == "__main__":
    test_time(main)