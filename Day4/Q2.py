with open("input.txt") as file:

    lines = file.readlines()

    num_x_mas = 0
    
    for y in range(1, len(lines)-1):
        line = lines[y]
        for x in range(1, len(lines[y])-1):
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
