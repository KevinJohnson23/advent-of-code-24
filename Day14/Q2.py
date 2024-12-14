from PerformanceTester.PerformanceTester import test_time

def main():
    with open("input.txt") as file:
        file_content = file.read()
    file_content = file_content.replace("p", "")
    file_content = file_content.replace("v", "")
    file_content = file_content.replace("=", "")

    robots = []

    for robot in file_content.split("\n"):
        robot_split = robot.split(" ")
        x, y = [int(c) for c in robot_split[0].split(",")]
        dx, dy = [int(c) for c in robot_split[1].split(",")]
        robots.append({
            "x": x,
            "y": y,
            "dx": dx,
            "dy": dy,
        })

    seconds = 0
    w, h = 101, 103
    num_robots = len(robots)

    while True:
        seconds += 1
        robot_positions = set()

        for robot in robots:
            dx, dy = robot["dx"], robot["dy"]

            robot["x"], robot["y"] = (robot["x"] + dx) % w, (robot["y"] + dy) % h
            robot_positions.add((robot["x"], robot["y"]))

        if len(robot_positions) == num_robots:
            break

    print(seconds)


if __name__ == "__main__":
    test_time(main)