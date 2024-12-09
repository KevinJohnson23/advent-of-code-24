with open("input.txt") as file:

    lines = file.read().split("\n\n")
    rules = [[int(x) for x in y.split("|")] for y in lines[0].split("\n")]
    updates = [[int(x) for x in y.split(",")] for y in lines[1].split("\n")]

    result = 0

    for update in updates:
        correct = True
        while True:
            n_swaps = 0
            for rule in rules:
                small = rule[0]
                big = rule[1]
            
                if small in update and big in update:
                    small_index = update.index(small)
                    big_index = update.index(big)
                    if small_index > big_index:
                        correct = False
                        update[big_index] = small
                        update[small_index] = big
                        n_swaps = 1
            if n_swaps == 0:
                break
                    
        if not correct:
            result += update[len(update)//2]

    print(result)
