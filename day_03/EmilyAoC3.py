import re
with open(r'C:\Users\emily\OneDrive\Documents\Maps\AOC\day_03.txt') as f:
    text = f.read()

found = re.findall("mul\(\d+,\d+\)", text)
digits_list = [re.findall("\d+", i) for i in found]
digits_list = [[int(e) for e in i] for i in digits_list]

total = 0

for pair in digits_list:
    for digit in range(len(pair) -1):
        total = total + (pair[digit] * pair[digit+1])

print(total)