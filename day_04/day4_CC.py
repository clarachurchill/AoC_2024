with open('day_04/input.txt') as f:
    text = f.read().split()

valid_paths = []
for y in range(-1, 2):
    for x in range(-1, 2):
        if not(x == 0 and y == 0):
            valid_paths.append([y, x])

x_paths = [x for x in valid_paths if 0 not in x]

length = len(text)
width = len(text[0])
xmas_joy = 0
xmas_x = 0
for y in range(length):
    for x in range(width):
        if text[y][x] == 'X':
            for dir in valid_paths:
                word = [text[y + dir[0] * mult][x + dir[1] * mult] for mult in list(range(0, 4)) if y + dir[0] * mult >= 0 and y + dir[0] * mult < length and x + dir[1] * mult >= 0 and x + dir[1] * mult < width]
                if ''.join(word) == 'XMAS' or ''.join(word) == 'SAMX':
                    xmas_joy += 1
        if text[y][x] == 'A':
            count_x = 0
            for dir in x_paths:
                word = [text[y + dir[0] * mult][x + dir[1] * mult] for mult in list(range(-1, 2)) if y + dir[0] * mult >= 0 and y + dir[0] * mult < length and x + dir[1] * mult >= 0 and x + dir[1] * mult < width]
                if ''.join(word) == 'MAS' or ''.join(word) == 'SAM':
                    count_x += 1
            if count_x == 4:
                xmas_x += 1
                    
print(xmas_joy)
print(xmas_x)
