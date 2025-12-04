import time

with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

def check_accessible_roll(lines: list[str], x: int, y: int) -> bool:
    counter = 0

    for y1 in range(y - 1, y + 2):
        if (y1 < 0 or y1 >= len(lines)):
            continue

        for x1 in range(x - 1, x + 2):
            if (x1 < 0 or x1 >= len(lines[0])):
                continue

            elif (x1 == x and y1 == y):
                continue

            if (lines[y1][x1] == '@'):
                counter += 1

    return  counter < 4

start_time = time.time()

roll_counter = 0
remaining_rolls = []

new_grid = []
for y in range(len(grid)):
    new_line = list()
    for x in range(len(grid[0])):

        if (grid[y][x] == '@' and check_accessible_roll(grid, x, y)):
            new_line.append('.')
            roll_counter += 1
            continue

        elif (grid[y][x] == '@'):
            remaining_rolls.append((x, y))

        new_line.append(grid[y][x])

    new_grid.append(new_line)

grid = new_grid

print("Part 1:", roll_counter)

while True:
    valid = False
    next_remaining = []

    for c in remaining_rolls:
        x = c[0]
        y = c[1]

        if (check_accessible_roll(grid, x, y)):
            valid = True
            roll_counter += 1
            grid[y][x] = '.'

        else:
            next_remaining.append((x, y))

    remaining_rolls = next_remaining

    if (not valid):
        break

print("Part 2:", roll_counter)

print("Elapsed:", time.time() - start_time, "seconds")