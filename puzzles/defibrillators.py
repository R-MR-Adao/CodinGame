import sys
from math import cos, sqrt

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def value(s):
    return float(s.replace(',','.'))

lon = value(input())
lat = value(input())
n = int(input())
defibs = []
for i in range(n):
    defib = input()
    defibInfo = defib.split(';')
    dLL = [value(defibInfo[-2]), value(defibInfo[-1])]
    #print("defibLongLat = {}".format(defibLongLat), file=sys.stderr, flush=True)
    x = (dLL[0] - lon)*cos((dLL[1] + lat)/2)
    y = dLL[1] - lat
    d = sqrt(x*x + y*y)*6371
    dName = defibInfo[1]
    defibs.append({'name':dName,'d':d})
print("defibs = {}".format(defibs), file=sys.stderr, flush=True)
dmin = -1
closest = defibs[0]
for defib in defibs:
    d = defib['d']
    if dmin < 0:
        dmin = d
    else:
        if d < dmin:
            dmin = d
            closest = defib

print(closest['name'])
