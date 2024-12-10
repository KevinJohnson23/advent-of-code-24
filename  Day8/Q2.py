from PerformanceTester.PerformanceTester import test_time

def is_inside(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

def get_antinodes(antinodes, x, y, w, h, dx, dy):
    while True:
        x += dx
        y += dy
        if not is_inside(x, y, w, h):
            break
        antinodes.add((x, y))

def main():
    with open("input.txt") as file:
        grid = [x.strip()for x in file]
        w, h = len(grid[0]), len(grid)

    antinodes = set()
    node_positions = dict()

    for y in range(h):
        for x in range(w):
            cell = grid[y][x]
            if cell.isalnum():
                if cell in node_positions:
                    node_positions[cell].append((x, y))
                else:
                    node_positions[cell] = [(x, y)]
                antinodes.add((x, y))

    for node, positions in node_positions.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                x, y = positions[i]
                x1, y1 = positions[j]
                dx, dy = x1-x, y1-y

                get_antinodes(antinodes, x, y, w, h, -dx, -dy)
                get_antinodes(antinodes, x1, y1, w, h, dx, dy)

    print(len(antinodes))

if __name__ == "__main__":
    test_time(main)