from PerformanceTester.PerformanceTester import test_time

def main():
    num_xmas = 0
    look_for = "MAS"
    with open("input.txt") as file:
        lines = file.readlines()
        tl_padding = len(look_for)-1
        br_padding = len(lines[0])-4

        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                if line[x] == "X":
                    y_greater = y > tl_padding
                    y_lesser = y < br_padding
                    if x > tl_padding:
                        if line[x-1] + line[x-2] + line[x-3] == look_for:
                            num_xmas += 1
                        if y_greater:
                            if lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == look_for:
                                num_xmas += 1
                        if y_lesser:
                            if lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == look_for:
                                num_xmas += 1
                    if x < br_padding:
                        if line[x+1] + line[x+2] + line[x+3] == look_for:
                            num_xmas += 1
                        if y_greater:
                            if lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == look_for:
                                num_xmas += 1
                        if y_lesser:
                            if lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == look_for:
                                num_xmas += 1
                    if y_greater:
                        if lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == look_for:
                            num_xmas += 1
                    if y_lesser:
                        if lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == look_for:
                            num_xmas += 1
    print(num_xmas)

if __name__ == "__main__":
    test_time(main)