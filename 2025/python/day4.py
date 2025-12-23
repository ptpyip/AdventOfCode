"""Advent of Code 2025 Day 4"""

def part1(puzzle_input):
    assert puzzle_input is not None

    puzzle_input = puzzle_input.lstrip("\n").rstrip("\n")
    print(f"there are {len(puzzle_input.split("\n"))} rows")

    grid = [list(row) for row in puzzle_input.split("\n")]
    grid_out = [list("." * len(grid[0])) for _ in range(len(grid))]  
    print(grid[0])

    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            
            if grid[y][x] == '@' and can_access(grid, (x, y)) :
                count += 1
                grid_out[y][x] = 'x'
            else:
                grid_out[y][x] = grid[y][x]

    print("\n".join(["".join(row) for row in grid_out]))
    print(count)

    return grid_out, count


def can_access(grid, pos) -> bool:
    """ Given a target position in the grid,
        return true if:
            there are fewer than 4 rolls of paper in the eight adjacent positions
    """
    assert len(pos) == 2 
    x, y = pos
    
    sum = 0
    start = (x-1, y-1)
    for i in range(3):
        for j in range(3):
            if (i == 1 and j == 1):
            #    or grid[x-1+i][y-1+j] != '@':
               continue
            
            current = (start[0] + i, start[1] + j)

            if is_paper_roll(grid, (x-1+i, y-1+j)):
                # print(f"\t{current} is paper roll")
                sum += 1
            # else:
                # print(f"\t{current} is NOT paper roll.")

    # print(f"There are {sum} rolls of paper adj. to {pos}")

    return sum < 4

def is_paper_roll(grid, pos: tuple) -> bool:
    """ Check if the target pos exists,
        If exits, return true if contains '@'.
        If not exists, return False.
    """
    assert len(pos) == 2 
    x, y = pos
    if x < 0 or x >= len(grid[0]):
        return False
    elif y < 0 or y >= len(grid):
        return False
    
    return grid[y][x] == '@'

def part2(puzzle_input):
    total_count = 0
    while True:
        grid_out, count = part1(puzzle_input)
        if count == 0:
            break
        total_count += count 
        puzzle_input = "\n".join(["".join(row) for row in grid_out])
    print(total_count)

if __name__ == "__main__":
    example_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    part1(example_input)
    part2(example_input)

    day4_input = ""
    with open("../inputs/day4.txt", 'r') as f:
       day4_input = "".join(f.readlines())

    # part1(day4_input)
    part2(day4_input)

