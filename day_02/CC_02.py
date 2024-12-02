with open('day_02/input.txt') as f:
    lines = f.readlines()
numbers = [x.strip().split(' ') for x in lines]

def test_line(line):
    for i in range(1, len(line)):
        if i > 1:
            curr_diff = line[i] - line[i - 1]
            old_diff = line[i - 1] - line[i - 2]
            if curr_diff * old_diff < 0:
                return False
        if abs(line[i] - line[i - 1]) not in [1, 2, 3]:
            return False
    return True

sol_one = 0
sol_two = 0
for line in numbers:
    line = [int(x) for x in line]
    if test_line(line):
        sol_one += 1
        sol_two += 1
    else:
        for x in range(len(line)):
            new_line = line.copy()
            del new_line[x]
            if test_line(new_line):
                sol_two += 1
                break
        
print(sol_one)
print(sol_two)
                