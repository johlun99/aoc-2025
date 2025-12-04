import time

with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

def check_accessible_roll(grid: list[list], x: int, y: int) -> bool:
    counter = 0

    for y2 in range(y - 1, y + 2):
        if (y2 < 0 or y2 >= len(grid)):
            continue

        for x2 in range(x - 1, x + 2):
            if (x2 < 0 or x2 >= len(grid[0])):
                continue

            elif (x2 == x and y2 == y):
                continue

            if (grid[y2][x2] == '@'):
                counter += 1

    return  counter < 4

start_time = time.time()

picked_rolls = 0
remaining_rolls = []

new_grid = []
for y in range(len(grid)):
    new_line = list()
    for x in range(len(grid[0])):

        if (grid[y][x] == '@' and check_accessible_roll(grid, x, y)):
            new_line.append('.')
            picked_rolls += 1
            continue

        elif (grid[y][x] == '@'):
            remaining_rolls.append((x, y))

        new_line.append(grid[y][x])

    new_grid.append(new_line)

grid = new_grid

print("Part 1:", picked_rolls)

next_grid = grid
while True:
    valid = False
    next_remaining = []

    for c in remaining_rolls:
        x = c[0]
        y = c[1]

        if (check_accessible_roll(grid, x, y)):
            valid = True
            picked_rolls += 1
            next_grid[y][x] = '.'

        else:
            next_remaining.append((x, y))

    remaining_rolls = next_remaining

    grid = next_grid
    if (not valid):
        break

print("Part 2:", picked_rolls)

print("Elapsed:", time.time() - start_time, "seconds")