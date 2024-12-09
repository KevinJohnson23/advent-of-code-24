from PerformanceTester.PerformanceTester import test_time

def main():
    result = 0
    current_string = ""
    do = True
    with open("input.txt") as file:
        for character in file.read():
            if character == ")":
                if current_string[:4] == "mul(":
                    if do:
                        numbers = current_string[4:].split(",")
                        if len(numbers) == 2:
                            num1 = numbers[0]
                            num2 = numbers[1]
                            if num1.isnumeric() and num2.isnumeric():
                                result += int(num1) * int(num2)
                elif current_string == "do(":
                    do = True
                elif current_string == "don't(":
                    do = False

            elif character in "md":
                current_string = ""
            current_string += character
    print(result)

if __name__ == "__main__":
    test_time(main)