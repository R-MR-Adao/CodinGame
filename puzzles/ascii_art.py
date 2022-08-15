import sys
import math

l = int(input())
h = int(input())
t = input()

key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
abc = {}
abc = {k:[] for k in key}
for i in range(h):
    row = input()
    for li in range(len(key)):
        abc[key[li]].append(row[li*l:(li+1)*l])

s = ['' for i in range(h)]

for c in t:
    for i in range(h):
        try:
            s[i] += abc[c.upper()][i]
        except:
            s[i] += abc['?'][i]

for line in s:
    print(line)

