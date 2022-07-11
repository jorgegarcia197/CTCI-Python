from tracemalloc import start


def sunsetViews(buildings, direction):
    # Write your code here.
    output = []
    max_height = 0
    start = len(buildings) - 1 if direction == "EAST" else 0
    stop = -1 if direction == "EAST" else len(buildings)
    step = -1 if direction == "EAST" else 1

    for i in range(start, stop, step):
        if buildings[i] > max_height:
            output.append(i)
            max_height = buildings[i]

    return sorted(output)


if __name__ == "__main__":
    buildings = [20, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8]
    print(sunsetViews(buildings, "EAST"))
