with open("input.txt") as file:

    lines = file.read().split("\n\n")
    rules = [[int(x) for x in y.split("|")] for y in lines[0].split("\n")]
    updates = [[int(x) for x in y.split(",")] for y in lines[1].split("\n")]

    result = 0

    for update in updates:
        correct = True
        for rule in rules:
            small = rule[0]
            big = rule[1]
            if small in update and big in update:
                if update.index(small) > update.index(big):
                    correct = False
                    break
        if correct:
            result += update[len(update)//2]

    print(result)
