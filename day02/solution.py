import time

with open("input.txt", "r") as f:
    line = ','.join([line.strip() for line in f.readlines()])

def is_repeating_once(s: str) -> bool:
    s1, s2 = s[:len(s) // 2], s[len(s) // 2:]

    return s1 == s2

def is_repeating(s: str) -> bool:
    return s in (s + s)[1:-1]

start_time = time.time()
ranges = [r for r in line.split(',')]

p1 = 0
p2 = 0

for r in ranges:
    s, e = r.split('-')

    for i in range(int(s), int(e) + 1):
        c = str(i)

        if (is_repeating_once(c)):
            p1 += int(c)
            p2 += int(c)

        elif(is_repeating(c)):
            p2 += int(c)

print("Elapsed:", time.time() - start_time, "seconds")
print("Part 1:", p1)
print("Part 2:", p2)