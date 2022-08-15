import sys
from math import atan, atan2
from numpy import diff, mean, where

# Save the Planet.
# Use less Fossil Fuel.

def sign(a):
    return a/abs(a)

n = int(input())  # the number of points used to draw the surface of Mars.
lx = []
ly = []
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    lx.append(land_x)
    ly.append(land_y)

# find flat splot
dy = diff(ly)
flat_i = where(dy == 0)[0]
print("flat_i = {}".format(flat_i), file=sys.stderr, flush=True)
flat_x0 = lx[flat_i[0]]
flat_x1 = lx[flat_i[-1]+1]
flat_x = mean([flat_x0, flat_x1])
flat_y = ly[flat_i[0]]
print("flat_x = {}, flat_y = {}".format(flat_x,flat_y), file=sys.stderr, flush=True)

# game loop
thrust_out = 3
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    dx = lx[flat_i[0]] - x
    dy = flat_y - y
    theta = atan2(dy,dx)/3.141*180
    print("Theta = {}, hs = {}, vs = {}, dy = {}".format(theta, hs, vs, dy), file=sys.stderr, flush=True)

    if flat_y < 1000:
        if x < flat_x0:
            theta_out = -15
        elif (flat_x0 <= x) and (x <= flat_x1):
            if hs > 0:
                theta_out = 10
            else:
                theta_out = -10
        else:
            theta_out = 15
        
        if hs > 0:
            if r > 5:
                thrust_out = 4
            if hs > 30:
                theta_out = 30
            elif hs > 25:
                theta_out = 10
            elif hs > 20:
                theta_out = 5
            else:
                thrust_out = 3
        elif hs < 0:
            if r < -5:
                thrust_out = 4
            if hs < - 30:
                theta_out = -50
            elif hs < -25:
                theta_out = -10
            elif hs < -20:
                theta_out = -5
            else:
                thrust_out = 3
            
            if x < flat_x0:
                theta_out += -7    
        

        if abs(vs) > 20:
            theta_out /= 2

        if abs(dy) < 1600:
            if abs(vs) > 19:
                #theta_out = theta_out/abs(theta_out) * max([4,theta_out])
                theta_out /= 2
                thrust_out = 4
            elif abs(vs) < 15:
                thrust_out = 3
        
    else:
        theta_out = 0
        thrust_out = 3
        if (((y < flat_y+10) or (y < flat_y + 500 and vs < 0)) and x > flat_x1) or (x < flat_x0 and ((y < flat_y+10) or (y < flat_y + 500 and vs < 0))):
            theta_out /=2
            thrust_out = 4
        
        if abs(hs) > 18:
            theta_out += 10 * sign(hs)
        
        if x < flat_x1:
            theta += 2

    if dy < 0 and abs(dy) < 40:
            theta_out = 0    
    print(' '.join([str(i) for i in [int(theta_out), thrust_out]]))
