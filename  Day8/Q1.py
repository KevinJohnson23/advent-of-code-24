from PerformanceTester.PerformanceTester import test_time

def is_inside(x, y, w, h):
    return 0 <= x < w and 0 <= y < h

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

    for node, positions in node_positions.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                x, y = positions[i]
                x1, y1 = positions[j]
                dx, dy = x1-x, y1-y
                px, py = x-dx, y-dy
                px1, py1 = x1+dx, y1+dy

                if is_inside(px, py, w, h):
                    antinodes.add((px, py))
                if is_inside(px1, py1, w, h):
                    antinodes.add((px1, py1))

    print(len(antinodes))

if __name__ == "__main__":
    test_time(main)