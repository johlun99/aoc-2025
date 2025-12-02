with open("input.txt", "r") as f:
    line = ','.join([line.strip() for line in f.readlines()])

def is_repeating_once(s: str) -> bool:
    f, s= s[:len(s) // 2], s[len(s) // 2:]

    return f== s

def is_repeating(s: str) -> bool:
    return s in (s + s)[1:-1]

ranges = [r for r in line.split(',') if r]

p1 = 0
p2 = 0

for r in ranges:
    start, end = r.split('-')

    for i in range(int(start), int(end) + 1):
        c = str(i)

        if (is_repeating_once(c)):
            p1 += int(c)
            p2 += int(c)

        elif(is_repeating(c)):
            p2 += int(c)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))