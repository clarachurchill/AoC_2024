import re
with open('day_03/input.txt') as f:
    text = f.read()

test_input = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
text_inputs = re.findall('mul\(([0-9]+),([0-9]+)\)', text)
print(sum([int(x[0])*int(x[1]) for x in text_inputs]))

donot_inputs = text.split("don't()")
do_inputs = ''.join([''.join(x.split('do()')[1:]) for x in donot_inputs if 'do' in x]) + donot_inputs[0]

do_inputs = re.findall('mul\(([0-9]+),([0-9]+)\)', do_inputs)
print(sum([int(x[0])*int(x[1]) for x in do_inputs]))
