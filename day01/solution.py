with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

c_num = 50
p1_count = 0
p2_count = 0

for l in lines:
    dir = l[0]
    num = int(l[1:])

    for i in range(num):
        if (dir == 'L'):
            c_num -= 1
        elif (dir == 'R'):
            c_num += 1

        if (c_num < 0):
            c_num = 99

        elif (c_num > 99):
            c_num = 0

        if (c_num == 0):
            p2_count += 1

    if (c_num == 0):
        p1_count += 1

print("Part 1: " + str(p1_count))
print("Part 2: " + str(p2_count))
