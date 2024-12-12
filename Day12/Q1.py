from PerformanceTester.PerformanceTester import test_time

def get_region(plots, x, y, plant, plot_positions):
    if plots[y][x] != plant:
        return

    plot_positions.add((x, y))

    if x > 0 and (x-1, y) not in plot_positions:
        get_region(plots, x-1, y, plant, plot_positions)
    if x < len(plots[0])-1 and (x+1, y) not in plot_positions:
        get_region(plots, x+1, y, plant, plot_positions)
    if y > 0 and (x, y-1) not in plot_positions:
        get_region(plots, x, y-1, plant, plot_positions)
    if y < len(plots)-1 and (x, y+1) not in plot_positions:
        get_region(plots, x, y+1, plant, plot_positions)

    return plot_positions

def get_adjacent(plot, x, y):
    adjacent = []
    if (x-1, y) in plot:
        adjacent.append((x-1, y))
    if (x+1, y) in plot:
        adjacent.append((x+1, y))
    if (x, y-1) in plot:
        adjacent.append((x, y-1))
    if (x, y+1) in plot:
        adjacent.append((x, y+1))
    return adjacent

def main():
    with open("input.txt") as file:
        plots = [list(line.strip()) for line in file]

    plots_positions = []
    positions_added = dict()
    for y in range(len(plots)):
        for x in range(len(plots[0])):
            if (x, y) in positions_added:
                continue
            plot_positions = get_region(plots, x, y, plots[y][x], set())
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
