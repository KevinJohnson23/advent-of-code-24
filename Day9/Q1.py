with open("input.txt") as file:
    disk_map = file.read().strip()

    file_layout = []
    current_id = 0
    for i in range(len(disk_map)):
        char = int(disk_map[i])
        if i % 2 == 0:
            for j in range(char):
                file_layout.append(current_id)
            current_id += 1
        else:
            for j in range(char):
                file_layout.append(None)

    last_file_position = len(file_layout)-1
    for i in range(len(file_layout)):
        if file_layout[i] == None:
            while file_layout[last_file_position] == None:
                last_file_position -= 1
            if last_file_position <= i:
                break
            file_layout[i] = file_layout[last_file_position]
            file_layout[last_file_position] = None

    result = 0
    for i in range(len(file_layout)):
        if file_layout[i] != None:
            result += i*file_layout[i]
        else:
            break

    print(result)