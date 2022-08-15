import sys
from numpy import floor

w, h, t1, t2, t3 = [int(i) for i in input().split()]
asts1 = {}
asts2 = {}
for i in range(h)
    r1, r2 = input().split()
    print(r1 +   + r2, file=sys.stderr, flush=True)
    for x,c in enumerate(r1)
        if c.isalpha() asts1[c] = [i,x]
        if r2[x].isalpha() asts2[r2[x]] = [i,x]

print(asts1, file=sys.stderr, flush=True)
print(asts2, file=sys.stderr, flush=True)

asts3 = {key  [int(floor(val[0] + (val[0] - asts1[key][0])(t2-t1)(t3-t2))), int(floor(val[1] + (val[1] - asts1[key][1])(t2-t1)(t3-t2)))] for key,val in asts2.items()}

print(asts3, file=sys.stderr, flush=True)

for i in range(h)
    s = list('.'w)
    for ast, pos in asts3.items()
        #xn = min([pos[1], len(s)-1])
        if pos[0] == i and 0 = pos[1] and pos[1]  len(s) and (ord(ast)  ord(s[pos[1]]) or s[pos[1]].isalpha() == False)
        #if pos[0] == i and (ord(ast)  ord(s[xn]) or s[xn].isalpha() == False)
            s[pos[1]] = ast
    print(.join(s))

