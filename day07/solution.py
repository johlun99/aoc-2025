grid = []
with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

s = ()
fs = False
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == 'S':
            fs = True
            s = (x, y)
            break

    if fs:
        break



def follow_line_p1(grid, found, pos) -> int:
    """Part 1: Count splits, avoiding previously passed lines."""
    x, y = pos

    while True:
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            break

        if (x, y) in found:
            break

        if grid[y][x] == '^':
            return 1 + follow_line_p1(grid, found, (x - 1, y)) + follow_line_p1(grid, found, (x + 1, y))

        found.add((x, y))
        y += 1

    return 0


def follow_line_p2(grid, pos, memo) -> int:
    """Part 2: Count all possible routes from pos to bottom, using memoization."""
    x, y = pos
    
    # Check bounds
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return 0
    
    # Check if we've already computed this position
    if (x, y) in memo:
        return memo[(x, y)]
    
    # If we're at the bottom, we've found one path
    if y == len(grid) - 1:
        memo[(x, y)] = 1
        return 1
    
    result = 0
    
    # Follow straight down until we hit a '^' or go out of bounds
    current_y = y
    while current_y < len(grid):
        # Check if current position is a '^'
        if grid[current_y][x] == '^':
            # Split into left and right
            result = follow_line_p2(grid, (x - 1, current_y), memo) + follow_line_p2(grid, (x + 1, current_y), memo)
            break
        # Move down one step
        current_y += 1
        # If we've reached the bottom, we found one path
        if current_y >= len(grid):
            result = 1
            break
    
    memo[(x, y)] = result
    return result


p1 = follow_line_p1(grid, set(), s)
print("Part 1:", p1)

p2 = follow_line_p2(grid, s, {})
print("Part 2:", p2)