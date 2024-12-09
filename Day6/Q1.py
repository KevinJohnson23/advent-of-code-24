def has_obstacle(path, x, y, w, h):
    if x in [-1, w] or y in [-1, h]:
        return False
    return path[y][x] == "#"

def get_distinct(path, start_x, start_y, w, h):
    current_x, current_y = start_x, start_y
    distinct = dict()
    while True:
        dx, dy = 0, 0
        distinct[current_x, current_y] = 1
        current = path[current_y][current_x]
        match current:
            case "^":
                if has_obstacle(path, current_x, current_y-1, w, h):
                    path[current_y][current_x] = ">"
                    continue
                dy = -1
            case ">":
                if has_obstacle(path, current_x+1, current_y, w, h):
                    path[current_y][current_x] = "v"
                    continue
                dx = 1
            case "v":
                if has_obstacle(path, current_x, current_y+1, w, h):
                    path[current_y][current_x] = "<"
                    continue
                dy = 1
            case "<":
                if has_obstacle(path, current_x-1, current_y, w, h):
                    path[current_y][current_x] = "^"
                    continue
                dx = -1
        
        if current_x+dx in [-1, w] or current_y+dy in [-1, h]:
            break

        path[current_y][current_x] = "."
        current_y += dy
        current_x += dx
        path[current_y][current_x] = current

    return len(distinct.keys())
    
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

    print(get_distinct(lines, start_x, start_y, w, h))
