with open('day_05/input.txt') as f:
    text = f.readlines()

text = [x.strip() for x in text]
map_dict = {}
start_input = True
for x, line in enumerate(text):
    if line == '':
        order_lists = text[x + 1:]
        break
        
    line = line.split('|')
    if int(line[0]) not in map_dict:
        map_dict[int(line[0])] = []
    map_dict[int(line[0])].append(int(line[1]))

order_lists = [x.split(',') for x in order_lists]
good_lists = [] 
bad_lists = []
for print_order in order_lists:
    failed = False
    print_order = [int(x) for x in print_order]
    for item in print_order:
        if item in map_dict:
            if any([print_order.index(item) > print_order.index(x) for x in map_dict[item] if x in print_order]):
                failed = True
    if failed:
        bad_lists.append(print_order)
    else:
        good_lists.append(print_order)  

print(sum([print_order[(len(print_order) - 1) // 2] for print_order in good_lists]))

fixed_lists = []
for print_order in bad_lists:
    new_order = []
    for item in print_order:
        index_list = [new_order.index(x) for x in map_dict[item] if x in new_order]
        if len(index_list) != 0:
            new_order.insert(min(index_list), item)
        else:
            new_order.append(item)
    fixed_lists.append(new_order)

print(sum([print_order[(len(print_order) - 1) // 2] for print_order in fixed_lists]))
