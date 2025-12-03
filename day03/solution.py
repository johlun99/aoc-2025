with open("input.txt", "r") as f:
    banks = [line.strip() for line in f.readlines()]

p1 = 0
for b in banks:
    hn1 = 0

    for i1 in range(len(b)):
        for i2 in range(i1 + 1, len(b)):
            if (int(b[i1] + b[i2]) > hn1):
                hn1 = int(b[i1] + b[i2])

    p1 += hn1

print("Part 1:", p1)

p2 = 0
for b in banks:
    n = len(b)
    k = 12
    
    if n < k:
        continue
    
    result = []
    last_pos = -1
    
    for pos in range(k):
        start = last_pos + 1
        end = n - (k - pos)
        
        max_digit = '0'
        max_idx = start
        for i in range(start, end + 1):
            if b[i] > max_digit:
                max_digit = b[i]
                max_idx = i
        
        result.append(max_digit)
        last_pos = max_idx
    
    joltage = int(''.join(result))
    p2 += joltage

print("Part 2:", p2)