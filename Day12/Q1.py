from PerformanceTester.PerformanceTester import test_time

def get_region(plots, x, y, plant, plot_positions, w, h):
    plot_positions.add((x, y))

    xm, xp, ym, yp = x-1, x+1, y-1, y+1

    if x > 0 and (xm, y) not in plot_positions and plots[y][xm] == plant:
        get_region(plots, xm, y, plant, plot_positions, w, h)
    if x < w and (xp, y) not in plot_positions and plots[y][xp] == plant:
        get_region(plots, x+1, y, plant, plot_positions, w, h)
    if y > 0 and (x, ym) not in plot_positions and plots[ym][x] == plant:
        get_region(plots, x, ym, plant, plot_positions, w, h)
    if y < h and (x, yp) not in plot_positions and plots[yp][x] == plant:
        get_region(plots, x, yp, plant, plot_positions, w, h)

def get_adjacent(plot, x, y):
    adjacent = []
    next_positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for next_x, next_y in next_positions:
        if (next_x, next_y) in plot:
            adjacent.append((next_x, next_y))
    return adjacent

def main():
    with open("input.txt") as file:
        plots = [line.strip() for line in file]
    w, h = len(plots[0])-1, len(plots)-1

    plots_positions = []
    positions_added = dict()
    for y in range(len(plots)):
        for x in range(len(plots[0])):
            if (x, y) in positions_added:
                continue
            plot_positions = set()
            get_region(plots, x, y, plots[y][x], plot_positions, w, h)
            plots_positions.append(plot_positions)
            for position in plot_positions:
                positions_added[position] = True

    price = 0
    for plot in plots_positions:
        area = len(plot)
        perimeter = 0
        for x, y in plot:
            perimeter += 4 - len(get_adjacent(plot, x, y))
        price += area * perimeter

    print(price)

if __name__ == "__main__":
    test_time(main)