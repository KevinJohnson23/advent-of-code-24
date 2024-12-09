from PerformanceTester.PerformanceTester import test_time

def is_safe(numbers):
    last_number = None
    ascending = None

    for n in numbers:
        if last_number is None:
            last_number = n
            continue
        n_larger = n > last_number
        if ascending is None:
            ascending = n_larger
        else:
            if ascending != n_larger:
                return False
        difference = abs(n - last_number)
        if difference < 1 or difference > 3:
            return False
        last_number = n
    return True

def main():
    with open("input.txt") as file:
        num_safe = 0
        for line in file:
            numbers = [int(n.strip()) for n in line.split()]
            if is_safe(numbers):
                num_safe += 1
            else:
                for i in range(len(numbers)):
                    n = numbers.pop(i)
                    if is_safe(numbers):
                        num_safe += 1
                        break
                    numbers.insert(i, n)
        print(num_safe)

if __name__ == "__main__":
    test_time(main)