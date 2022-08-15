
w, h = [int(i) for i in input().split()]
y0, x0 = [int(i) for i in input().split()]
n = int(input())
move = {'v': [0,  1], '<': [-1, 0], '^': [0, -1], '>': [1,  0]}
lens = []
found = False
for i in range(n):
    m = []
    x = x0
    y = y0
    xy = [[x0, y0]]
    l = 1
    m = [ [c for c in input()] for j in range(h)]
    while m[y][x] in 'v<^>':
        dx, dy = move[m[y][x]]
        x += dx
        y += dy
        l += 1
        if [x, y] in xy: break                        # waking in circles
        else:            xy.append([x, y])
        if x < 0 or w <= x or y < 0 or h <= y:        # out of bounds
            x = x0
            y = y0
            break
    if m[y][x] == 'T':
        found = True
        lens.append(l)
    else:
        lens.append(100000000000)
if(found):
    print(lens.index(min(lens)))
else:
    print('TRAP')
