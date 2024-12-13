with open('day_02/input.txt') as f:
    lines = f.readlines()
safety_values = [list(map(int, x.strip().split(' '))) for x in lines]

print(safety_values)
results = 0

for i in safety_values:
    sign = []
    difference = []
    for e in range(len(i) -1):
        if i[e] - i[e+1] > 0:
            sign.append("Positive")
        else:
            sign.append("Negative")
    for e in range(len(i) -1):
        if abs(i[e] - i[e+1]) in range(1, 4):
            difference.append("Yes")
        else:
            difference.append("No") 
    if len(set(sign)) == 1 and "No" not in difference:
            results = results+1

print(results)
