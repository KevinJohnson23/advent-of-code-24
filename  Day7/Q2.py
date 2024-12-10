from PerformanceTester.PerformanceTester import test_time

def calculate_next(current, numbers):
    if len(numbers) == 1:
        return current in numbers

    popped = numbers.pop()
    if current % popped == 0:
        if calculate_next(current // popped, numbers.copy()):
            return True
    if str(current).endswith(str(popped)) and current != popped:
        if calculate_next(int(str(current)[:len(str(current))-len(str(popped))]), numbers.copy()):
            return True
    if current - popped > 0:
        if calculate_next(current-popped, numbers.copy()):
            return True

def main():
    result = 0

    with open("input.txt") as file:
        for line in file:
            line_numbers = [int(x) for x in line.strip().replace(":", "").split(" ")]

            expecting = line_numbers[0]
            values = line_numbers[1:]

            if calculate_next(expecting, values):
                result += expecting

    print(result)

if __name__ == "__main__":
    test_time(main)