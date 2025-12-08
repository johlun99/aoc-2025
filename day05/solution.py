ranges = []
ingredients = []

with open("input.txt") as f:
    for line in f:
        l = line.strip()
        if not l:
            continue
        if "-" in l:
            start_s, end_s = l.split("-", 1)
            ranges.append((int(start_s), int(end_s)))
        elif l.isdecimal():
            ingredients.append(int(l))

fresh_ingredients = []

for x in ingredients:
    for start, end in ranges:
        if x >= start and x <= end and x not in fresh_ingredients:
            fresh_ingredients.append(x)

print("Part 1:", len(fresh_ingredients))

ranges = sorted(ranges)
total = 0

cur_start, cur_end = ranges[0]
for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        total += cur_end - cur_start + 1
        cur_start, cur_end = start, end

total += cur_end - cur_start + 1
print("Part 2:", total)