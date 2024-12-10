from PerformanceTester.PerformanceTester import test_time

def go_to_next(path, x, y, w, h):
    current = int(path[y][x])
    if current == 9:
        return 1

    nines = 0
    if x > 0 and int(path[y][x-1]) - current == 1:
        nines += go_to_next(path, x-1, y, w, h)
    if x < w - 1 and int(path[y][x+1]) - current == 1:
        nines += go_to_next(path, x + 1, y, w, h)
    if y > 0 and int(path[y-1][x]) - current == 1:
        nines += go_to_next(path, x, y - 1, w, h)
    if y < h-1 and int(path[y+1][x]) - current == 1:
        nines += go_to_next(path, x, y + 1, w, h)
    return nines

def main():
    result = 0
    with open("input.txt") as file:
        lines = [line.strip() for line in file]
        h, w = len(lines), len(lines[0])
        for y in range(h):
            for x in range(w):
                if lines[y][x] == "0":
                    result += go_to_next(lines, x, y, w, h)
    print(result)

if __name__ == "__main__":
    test_time(main)
