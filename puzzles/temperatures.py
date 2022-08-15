import sys

n = int(input())  # the number of temperatures to analyse
if n > 0:
    t = []
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t.append(int(i))
    ta = list(map(abs,t))
    tm = [t[i] for i,x in enumerate(ta) if x == min(ta)]
    print(max(tm))
else:
    print(0)
