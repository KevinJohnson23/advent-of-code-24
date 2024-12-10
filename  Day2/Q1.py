from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        num_safe = 0

        for line in file:
            numbers = map(int, line.split())
            last_number = None
            ascending = None
            safe = True

            for n in numbers:
                if last_number is None:
                    last_number = n
                    continue
                n_larger = n > last_number
                if ascending is None:
                    ascending = n_larger
                else:
                    if ascending != n_larger:
                        safe = False
                        break
                difference = abs(n - last_number)
                if difference < 1 or difference > 3:
                    safe = False
                    break
                last_number = n

            if safe:
                num_safe += 1
        print(num_safe)

if __name__ == "__main__":
    test_time(main)