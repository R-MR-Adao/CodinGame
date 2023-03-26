import numpy as np

# ex_y: floor on which the exit is found
# ex_x: position of the exit on its floor
# n_elv: number of elevators
_ , _ , _, ex_y, ex_x, _, _ , n_elv = [int(i) for i in input().split()]

# elevs: matrix with elevator coordinates
elevs = np.array([[int(j) for j in input().split()] for i in range(n_elv)])

dr_sign = {'LEFT':-1,'RIGHT':1} # direction sign

# game loop
while True:
    out = "WAIT"
    # c_y: floor on which the leading clone is found
    # c_x: position of the leading clone
    # dr: direction ('LEFT' or 'RIGHT')
    c_y, c_x, dr = [int(s) if i < 2 else s for i,s in enumerate(input().split())]

    if dr != "NONE":                        # clones available
        if c_y == ex_y:                     # in exit floor
            d = ex_x - c_x                  # distance to exit
        else:                               # wrong floor: find elevator
            elev_x = elevs[np.argmax(elevs[:,0]==c_y),1]    # elevator position
            d = elev_x - c_x                # distance to elevator
        if d * dr_sign[dr] < 0:             # going in the wrong direction
            out = 'BLOCK'

    print(out)                              # action: WAIT or BLOCK
