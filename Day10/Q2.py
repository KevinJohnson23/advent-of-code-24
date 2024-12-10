from PerformanceTester.PerformanceTester import test_time

def go_to_next(path, x, y, visited=set(), previous=None):
    current = path[y][x]

    if previous and int(current) - int(previous) != 1:
        return {}
    if current == "9":
        return {(x, y)}

    positions = set()
    if x > 0:
        positions.add((x - 1, y))
    if x < len(path[0]) - 1:
        positions.add((x + 1, y))
    if y > 0:
        positions.add((x, y-1))
    if y < len(path)-1:
        positions.add((x, y+1))

    visited.add((x, y))

    nines = []
    for position in positions:
        if position not in visited:

            nine_positions = go_to_next(path, position[0], position[1], visited.copy(), current)
            for nine_position in nine_positions:
                nines.append(nine_position)

    return nines

def main():
    result = 0
    with open("input.txt") as file:
        lines = [line.strip() for line in file]
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == "0":
                    nines = go_to_next(lines, x, y)
                    for nine in nines:
                        if nine is None:
                            continue
                        result += 1
    print(result)

if __name__ == "__main__":
    test_time(main)
