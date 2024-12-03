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

#now let's do it without any imports - my challenge for AoC
def find_mul(text):
    out = []
    while 'mul(' in text:
        mul_start = text.index('mul(')
        text = text[mul_start + 4:]
        if ',' in text:
            mul_text = text.split(',')           
            if ')' in mul_text[1]:
                try:
                    int_one = int(mul_text[0])
                    int_two = int(mul_text[1].split(')')[0])
                except:
                    continue
                out.append((int_one, int_two))
    return out

print(sum([x[0]*x[1] for x in find_mul(text)]))

donot_inputs = text.split("don't()")
do_inputs = ''.join([''.join(x.split('do()')[1:]) for x in donot_inputs if 'do' in x]) + donot_inputs[0]

print(sum([x[0] * x[1] for x in find_mul(do_inputs)]))
