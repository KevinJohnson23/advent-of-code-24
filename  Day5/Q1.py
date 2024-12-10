from PerformanceTester.PerformanceTester import test_time

def main():
    result = 0
    with open("input.txt") as file:
        lines = file.read().split("\n\n")
        rules = [[int(x) for x in y.split("|")] for y in lines[0].splitlines()]
        updates = [list(map(int, y.split(","))) for y in lines[1].splitlines()]

        for update in updates:
            correct = True
            for rule in rules:
                small = rule[0]
                big = rule[1]
                if small in update and big in update:
                    if update.index(small) > update.index(big):
                        correct = False
                        break
            if correct:
                result += update[len(update)//2]
    print(result)

if __name__ == "__main__":
    test_time(main)