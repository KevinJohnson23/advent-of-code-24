from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        left = []
        right = []
        for line in file.readlines():
            line_split = line.split("   ")
            left.append(int(line_split[0]))
            right.append(int(line_split[1]))

        similarity = 0
        for nl in left:
            appearances = 0
            for nr in right:
                if nl == nr:
                    appearances += 1
            similarity += nl*appearances

        print(similarity)

if __name__ == "__main__":
    test_time(main)