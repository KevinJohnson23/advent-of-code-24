with open("input.txt") as file:

    lines = file.readlines()

    num_xmas = 0
    look_for = "MAS"
    tl_padding = len(look_for)-1
    br_padding = len(lines[0])-4
    
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(lines[y])):
            if line[x] == "X":
                if x > tl_padding:
                    if line[x-1] + line[x-2] + line[x-3] == look_for:
                        num_xmas += 1
                    if y > tl_padding:
                        if lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == look_for:
                            num_xmas += 1
                    if y < br_padding:
                        if lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == look_for:
                            num_xmas += 1
                if x < br_padding:
                    if line[x+1] + line[x+2] + line[x+3] == look_for:
                        num_xmas += 1
                    if y > tl_padding:
                        if lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == look_for:
                            num_xmas += 1
                    if y < br_padding:
                        if lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == look_for:
                            num_xmas += 1
                if y > tl_padding:
                    if lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == look_for:
                        num_xmas += 1
                if y < br_padding:
                    if lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == look_for:
                        num_xmas += 1
    print(num_xmas)
