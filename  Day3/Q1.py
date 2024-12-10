from PerformanceTester.PerformanceTester import test_time

def main():
    result = 0
    current_string = ""
    with open("input.txt") as file:
        for character in file.read():
            if character == ")":
                if current_string[:4] == "mul(":
                    numbers = [current_string[4:].split(",")]
                    if len(numbers) == 2:
                        num1 = numbers[0]
                        num2 = numbers[1]
                        if num1.isnumeric() and num2.isnumeric():
                            result += int(num1) * int(num2)
                current_string = ""
            elif character == "m":
                current_string = "m"
            else:
                current_string += character
    print(result)

if __name__ == "__main__":
    test_time(main)