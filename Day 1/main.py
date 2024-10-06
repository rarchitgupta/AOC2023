import os

# Part 1
def part_1(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        input = f.readlines()

    ans = 0

    for line in input:
        first = None
        last = None
        for c in line:
            if c.isdigit() and first is None:
                first = c
            if c.isdigit():
                last = c
        
        num = int(first + last)
        ans += num
    
    return ans