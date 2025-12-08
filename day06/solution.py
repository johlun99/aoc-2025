numbers = []
operators = []

with open("sample-input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    for l in lines:
        parts = [n for n in l.split(' ') if n]

        for i in range(len(parts)):
            if i == len(numbers):
                numbers.append([])

            if (parts[i].isdecimal()):
                numbers[i].append(parts[i])

            else:
                operators.append(parts[i])


print(numbers)
print(operators)

p1 = 0

for e in range(len(operators)):
    eq = ""
    for n in numbers[e]:
        eq += str(n) + operators[e]

    eq = eq[:-1]

    p1 += eval(eq)

print("Part 1:", p1)

p2 = 0
for e in range(len(operators) - 1, -1, -1):
    op = operators[e]
    longest = 0
    for n in numbers[e]:
        if len(n) > longest:
            longest = len(n)

    eq = ""
    '''
    print("Longest:", longest)
    print(numbers[e])
    '''

    for i in range(longest - 1, -1, -1):
        num = ""

        for n in numbers[e]:
            if i < len(n):
                num += str(n[i])

        print("Num:", num)

        eq += str(num) + op

    print("eq", eq)
    p2 += eval(eq[:-1])

print("Part 2", p2)