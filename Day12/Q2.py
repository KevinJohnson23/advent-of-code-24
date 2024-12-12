from PerformanceTester.PerformanceTester import test_time

def get_region(plots, x, y, plant, plot_positions):
    if plots[y][x] != plant:
        return

    plot_positions.append((x, y))

    if x > 0 and (x-1, y) not in plot_positions:
        get_region(plots, x-1, y, plant, plot_positions)
    if x < len(plots[0])-1 and (x+1, y) not in plot_positions:
        get_region(plots, x+1, y, plant, plot_positions)
    if y > 0 and (x, y-1) not in plot_positions:
        get_region(plots, x, y-1, plant, plot_positions)
    if y < len(plots)-1 and (x, y+1) not in plot_positions:
        get_region(plots, x, y+1, plant, plot_positions)

    return plot_positions

def main():
    with open("input.txt") as file:
        plots = [list(line.strip()) for line in file]

    plots_positions = []
    positions_added = set()
    for y in range(len(plots)):
        for x in range(len(plots[0])):
            if (x, y) in positions_added:
                continue
            plot_positions = get_region(plots, x, y, plots[y][x], [])
            plots_positions.append(plot_positions)
            for position in plot_positions:
                positions_added.add(position)

    price = 0
    for plot in plots_positions:
        area = len(plot)

        corners = []

        for x, y in plot:
            #Convex corner
            if (x-1, y) not in plot and (x, y-1) not in plot:
                corners.append((x, y))
            if (x+1, y) not in plot and (x, y+1) not in plot:
                corners.append((x+1, y+1))
            if (x, y-1) not in plot and (x+1, y) not in plot:
                corners.append((x+1, y))
            if (x-1, y) not in plot and (x, y+1) not in plot:
                corners.append((x, y+1))

            #Concave corner
            if (x-1, y) in plot and (x, y-1) in plot and (x-1, y-1) not in plot:
                corners.append((x, y))
            if (x+1, y) in plot and (x, y-1) in plot and (x+1, y-1) not in plot:
                corners.append((x+1, y))
            if (x+1, y) in plot and (x, y+1) in plot and (x+1, y+1) not in plot:
                corners.append((x+1, y+1))
            if (x-1, y) in plot and (x, y+1) in plot and (x-1, y+1) not in plot:
                corners.append((x, y+1))

        sides = len(corners)
        price += area * sides

    print(price)

if __name__ == "__main__":
    test_time(main)
