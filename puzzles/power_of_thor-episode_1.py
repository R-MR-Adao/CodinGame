import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
tx = initial_tx
ty = initial_ty
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # A single line providing the move to be made: N NE E SE S SW W or NW
    dif_x = light_x - tx
    dif_y = light_y - ty
    
    # directions
    c1 = ''
    c2 = ''
    offx = 0
    offy = 0
    
    # decide between north and south
    if dif_y > 0:
        c1 = 'S'
        offy = 1
    elif dif_y == 0:
        c1 = ''
    else:
        c1 = 'N'
        offy = -1
    
    # decide between East and west
    if dif_x > 0: 
        c2 = 'E'
        offx = 1
    elif dif_x == 0:
        c2 = ''
    else:
        c2 = 'W'
        offx = -1
    
    direction = c1+c2
    tx = tx + offx
    ty = ty + offy
    
    print(direction)
