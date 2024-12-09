from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        left = []
        right = []
        for line in file.readlines():
            line_split = [int(x.strip()) for x in line.split()]
            left.append(line_split[0])
            right.append(line_split[1])

        left.sort()
        right.sort()

        total = 0
        for i in range(len(left)):
            total += abs(left[i] - right[i])

        print(total)

if __name__ == "__main__":
    test_time(main)