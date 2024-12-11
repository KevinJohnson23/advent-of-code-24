from PerformanceTester.PerformanceTester import test_time

def create_file_layout(disk_map):
    file_layout = []
    free_intervals_size_map = dict()
    file_intervals = []
    current_id = 0

    for i in range(len(disk_map)):
        char = int(disk_map[i])
        if i % 2 == 0:
            file_intervals.insert(0, (len(file_layout), len(file_layout) + char - 1))
            file_layout.extend([current_id] * char)
            current_id += 1
        else:
            current_num_files = len(file_layout)
            if char > 0:
                free_interval = [current_num_files, current_num_files + char - 1]
                if char in free_intervals_size_map:
                    free_intervals_size_map[char].append(free_interval)
                else:
                    free_intervals_size_map[char] = [free_interval]

            file_layout.extend([None] * char)

    return file_layout, free_intervals_size_map, file_intervals

def get_free_size(free_intervals_size_map, file_size, file_end):
    free_size = None
    for free_interval_size in free_intervals_size_map:
        if free_interval_size < file_size:
            continue
        free_intervals = free_intervals_size_map[free_interval_size]
        if len(free_intervals) == 0 or free_intervals[0][0] >= file_end:
            continue
        if free_size is None or free_intervals_size_map[free_interval_size][0][0] < \
                free_intervals_size_map[free_size][0][0]:
            free_size = free_interval_size
    return free_size

def main():
    with open("input.txt") as file:
        disk_map = file.read().strip()

    file_layout, free_intervals_size_map, file_intervals = create_file_layout(disk_map)

    for file_start, file_end in file_intervals:

        file_size = file_end - file_start + 1
        free_size = get_free_size(free_intervals_size_map, file_size, file_end)
        if not free_size:
            continue
        free_interval = free_intervals_size_map[free_size].pop(0)

        for i in range(file_size):
            file_layout[free_interval[0]+i] = file_layout[file_start+i]
            file_layout[file_start+i] = None
        free_interval[0] += file_size

        if free_interval[0] <= free_interval[1]:
            new_free_size = free_interval[1] - free_interval[0] + 1

            if new_free_size in free_intervals_size_map:

                if len(free_intervals_size_map[new_free_size]) > 0:
                    current_free_size_index = 0
                    while True:
                        if current_free_size_index >= len(free_intervals_size_map[new_free_size]):
                            free_intervals_size_map[new_free_size].append(free_interval)
                            break
                        if free_intervals_size_map[new_free_size][current_free_size_index][0] > free_interval[0]:
                            free_intervals_size_map[new_free_size].insert(current_free_size_index, free_interval)
                            break
                        current_free_size_index += 1
                else:
                    free_intervals_size_map[new_free_size].append(free_interval)
            else:
                free_intervals_size_map[new_free_size] = [free_interval]

    result = 0
    for i in range(len(file_layout)):
        if file_layout[i] is not None:
            result += i*file_layout[i]

    print(result)

if __name__ == "__main__":
    test_time(main)