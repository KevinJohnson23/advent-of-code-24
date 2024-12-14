from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        file_content = file.read()
    file_content = file_content.replace("p", "")
    file_content = file_content.replace("v", "")
    file_content = file_content.replace("=", "")

    seconds = 100
    w, h = 101, 103
    robot_positions = dict()

    for robot in file_content.split("\n"):
        robot_split = robot.split(" ")
        x, y = [int(c) for c in robot_split[0].split(",")]
        dx, dy = [int(c) for c in robot_split[1].split(",")]

        new_x, new_y = (x + dx * seconds) % w, (y + dy * seconds) % h
        robot_positions[new_x, new_y] = robot_positions.get((new_x, new_y), 0) + 1

    safety_factor = 1
    w_half, h_half = w // 2, h // 2

    for i in range(4):
        num_robots = 0

        for x in range(w_half):
            for y in range(h_half):

                current_x, current_y = x, y
                if i == 1:
                    current_x += w_half + 1
                elif i == 2:
                    current_y += h_half + 1
                elif i == 3:
                    current_x += w_half + 1
                    current_y += h_half + 1

                if (current_x, current_y) in robot_positions:
                    num_robots += robot_positions[current_x, current_y]

        safety_factor *= num_robots

    print(safety_factor)

if __name__ == "__main__":
    test_time(main)