from PerformanceTester.PerformanceTester import test_time

def main():
    left, right = [], []
    with open("input.txt") as file:
        for line in file:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)
    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    print(total)

if __name__ == "__main__":
    test_time(main)