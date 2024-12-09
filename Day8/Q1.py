from itertools import product

def is_inside(x, y, w, h):
    return x >= 0 and x < w and y >= 0 and y < h

with open("input.txt") as file:
    grid = [list(x.strip()) for x in file.readlines()]
    w, h = len(grid[0]), len(grid)
    positions = list(product(range(w), range(h)))
    
    antinodes = set()

    for x, y in positions:
        cell = grid[y][x]

        if cell.isalnum():

            for x1, y1 in positions:
                if (x, y) == (x1, y1):
                    continue

                cell1 = grid[y1][x1]
                if cell == cell1:
                    dx, dy = x1-x, y1-y
                    px, py = x-dx, y-dy
                    px1, py1 = x1+dx, y1+dy

                    if is_inside(px, py, w, h):
                        antinodes.add((px, py))
                    if is_inside(px1, py1, w, h):
                        antinodes.add((px1, py1))

    print(len(antinodes))