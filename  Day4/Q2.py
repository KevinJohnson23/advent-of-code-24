from PerformanceTester.PerformanceTester import test_time

def main():
    num_x_mas = 0
    with open("input.txt") as file:
        lines = file.readlines()
        h,w = len(lines)-1, len(lines[0])-1
        for y in range(1, h):
            line = lines[y]
            for x in range(1, w):
                if line[x] == "A":
                    if (
                        ((lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or
                        (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M"))
                        and
                        ((lines[y+1][x-1] == "M" and lines[y-1][x+1] == "S") or
                        (lines[y+1][x-1] == "S" and lines[y-1][x+1] == "M"))
                    ):
                        num_x_mas += 1
    print(num_x_mas)

if __name__ == "__main__":
    test_time(main)
