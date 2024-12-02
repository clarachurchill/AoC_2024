with open('day_01/input.txt') as f:
    lines = f.readlines()
    numbers = [x.strip().split('   ') for x in lines]
list_one = [int(x[0]) for x in numbers]
list_two = [int(x[1]) for x in numbers]

list_one.sort()
list_two.sort()

differences = [abs(x - y) for x, y in zip(list_one, list_two)]
print(sum(differences))

occurences = sum([x * list_two.count(x) for x in list_one])
print(occurences)