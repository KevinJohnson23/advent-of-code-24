from PerformanceTester.PerformanceTester import test_time
from collections import Counter

def main():
    left, right = [], []
    with open("input.txt") as file:
        for line in file:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

    right_count = Counter(right)
    similarity = 0
    for l in left:
        similarity += l * right_count.get(l, 0)
    print(similarity)

if __name__ == "__main__":
    test_time(main)