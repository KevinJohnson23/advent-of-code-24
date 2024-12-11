from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        disk_map = file.read().strip()

    file_layout = []
    free_intervals = []
    current_id = 0

    for i in range(len(disk_map)):
        char = int(disk_map[i])
        if i % 2 == 0:
            file_layout.extend([current_id] * char)
            current_id += 1
        else:
            current_num_files = len(file_layout)
            free_intervals.append((current_num_files, current_num_files+char))
            file_layout.extend([None] * char)

    last_file_position = len(file_layout) - 1
    for start, end in free_intervals:
        for i in range(start, end):
            while file_layout[last_file_position] is None:
                last_file_position -= 1
            if last_file_position <= i:
                break
            file_layout[i] = file_layout[last_file_position]
            file_layout[last_file_position] = None
        if last_file_position <= i:
            break

    result = 0
    for i in range(len(file_layout)):
        if file_layout[i] is None:
            break
        else:
            result += i * file_layout[i]

    print(result)

if __name__ == "__main__":
    test_time(main)