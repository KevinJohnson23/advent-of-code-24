with open("input.txt") as file:
    left = []
    right = []
    for line in file.readlines():
        line_split = line.split("   ")
        left.append(int(line_split[0]))
        right.append(int(line_split[1]))

    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])

    print(total)