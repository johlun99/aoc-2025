with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def check_accessible_roll(lines: list[str], x: int, y: int):
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

p1 = True
roll_counter = 0

while True:
    output = []
    c_counter = 0
    for y in range(len(lines)):
        o_line = ""
        for x in range(len(lines[0])):
            if lines[y][x] == '.':
                o_line += '.'
                continue

            if (check_accessible_roll(lines, x, y)):
                o_line += '.'
                roll_counter += 1
                c_counter += 1

            else:
                o_line += '@'

        output.append(o_line)

    lines = output

    if (p1):
        print("Part 1:", roll_counter)
        p1 = False

    if (c_counter <= 0):
        break

print("Part 1:", roll_counter)