import sys
import math
from statistics import mean

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

w0 = 0  # dynamic world limits
w1 = w  # dynamic world limits
h0 = 0  # dynamic world limits
h1 = h  # dynamic world limits
x = x0  # current position
y = y0  # current position
x1 = x0 # instatiate next position
y1 = y0 # instatiate next position
ii = 1  # iteration
def dirs(key):
    dirs = {
        'U' : [-1, h0],
        'UR': [w1, h0],
        'R' : [w1, -1],
        'DR': [w1, h1],
        'D' : [-1, h1],
        'DL': [w0, h1],
        'L' : [w0, -1],
        'UL': [w0, h0]
    }
    return dirs[key]

def move(xy,m,f,xymin,xymax):
    off = (mean([xy,m]) - xy) #/ max([1,f/4])
    if abs(off) < 1:
        off = off/abs(off)
    if off > 0:
        xymin = xy
    if off < 0:
        xymax = xy
    return round(xy + round(off)), xymin, xymax

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    mf = dirs(bomb_dir)

    if mf[0] >= 0:
        x1, w0, w1 = move(x,mf[0],ii,w0,w1)
    if mf[1] >= 0:
        y1, h0, h1 = move(y,mf[1],ii,h0,h1)

    x = x1 # update position
    y = y1 # update position
    ii += 1 # update iteration
    # the location of the next window Batman should jump to.
    print('{} {}'.format(x1, y1))
