from itertools import product

op = ["*", "+"]

with open("input.txt") as file:
    result = 0

    for line in file.readlines():
        numbers = [int(x) for x in line.replace(":", "").replace("\n", "").split(" ")]
        expecting = numbers[0]
        set_numbers = numbers[1:]

        operators = product(op, repeat=len(set_numbers)-1)
    
        for ops in operators:
            curr = numbers[1]
            for i, operator in enumerate(ops):
                if operator == "*":
                    curr *= set_numbers[i+1]
                elif operator == "+":
                    curr += set_numbers[i+1]
                else:
                    curr = int(str(curr)+str(set_numbers[i+1]))
            if curr == expecting:
                result += expecting
                break
    
    print(result)