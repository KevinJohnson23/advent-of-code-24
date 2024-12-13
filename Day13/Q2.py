from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        file_content = file.read()
    file_content = file_content.replace("Button A: ", "")
    file_content = file_content.replace("Button B: ", "")
    file_content = file_content.replace("Prize: ", "")
    file_content = file_content.replace("X", "")
    file_content = file_content.replace("Y", "")
    file_content = file_content.replace("+", "")
    file_content = file_content.replace("=", "")
    file_content = file_content.replace(" ", "")

    tokens = 0
    offset = 10000000000000

    for game in file_content.split("\n\n"):
        a, b, prize = game.split("\n")
        xa, ya = [int(c) for c in a.split(",")]
        xb, yb = [int(c) for c in b.split(",")]
        xp, yp = [int(c)+offset for c in prize.split(",")]

        u = (xp * yb - yp * xb) / (xa * yb - ya * xb)
        if int(u) != u:
            continue
        u = int(u)
        v = (xp - u * xa) // xb

        tokens += u * 3 + v

    print(tokens)

if __name__ == "__main__":
    test_time(main)