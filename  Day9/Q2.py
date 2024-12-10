def get_free_intervals(file_layout):
    free_intervals = []

    free_start = None
    free_end = None

    for i in range(len(file_layout)):
        if file_layout[i] == None:
            free_start = i if free_start == None else free_start
            free_end = i

        elif free_start != None:

            free_intervals.append([free_start, free_end])

            free_start = None
            free_end = None

    return free_intervals

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

    file_start = None
    file_end = None

    free_intervals = get_free_intervals(file_layout)

    for j in range(len(file_layout)-1, -1, -1):
        if file_start == None or file_layout[file_start] == None:
            file_start = j
        if file_start != None and file_layout[j] != None and file_layout[file_start] == file_layout[j]:
            file_end = j

        if file_start != None and file_layout[j] != file_layout[file_start]:

            file_length = file_start-file_end

            for i in range(len(free_intervals)):
                free_interval = free_intervals[i]
                if free_interval == None or free_interval[0] >= file_end:
                    continue
                free_start = free_interval[0]
                free_end = min(free_interval[1], file_end-1)

                free_length = free_end-free_start
                if free_length >= file_length:

                    for k in range(file_length+1):
                        file_layout[free_start+k] = file_layout[file_start-k]
                        file_layout[file_start-k] = None
                    free_intervals[i][0] += file_length+1
                    if free_intervals[i][0] > free_intervals[i][1]:
                        free_intervals[i] = None
                    break

            file_start = j
            file_end = j

    result = 0
    for i in range(len(file_layout)):
        if file_layout[i] != None:
            result += i*file_layout[i]

    print(result)