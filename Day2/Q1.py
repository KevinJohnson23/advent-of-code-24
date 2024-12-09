with open("input.txt") as file:
    num_safe = 0

    for line in file.readlines():
        numbers = [int(n) for n in line.split(" ")]

        last_number = numbers[0]
        ascending = None
        safe = True
        
        for n in numbers[1:]:
            n_larger = n > last_number
            if ascending == None:
                ascending = n_larger
            else:
                if ascending and not n_larger or n_larger and not ascending:
                    safe = False
                    break
            difference = n - last_number if ascending else last_number - n
            if difference < 1 or difference > 3:
                safe = False
                break
            last_number = n
            
        if safe:
            num_safe += 1

    print(num_safe)
