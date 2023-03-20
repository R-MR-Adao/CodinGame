import numpy as np

width = int(input())    # the number of cells on the X axis
height = int(input())   # the number of cells on the Y axis
w_map = np.array([[j for j in input()] for i in range(height)]) # width characters, each either 0 or .

s_out = ''              # output string
for y, line in enumerate(w_map):
    x_off = 0                                                   # x offset
    while len(line) > 0:                                        # line becomes shorter as we go
        n = line[line == '0']                                   # find nodes in line
        if len(n) > 0:                                          # nodes were found
            x = np.argmin(line != '0') + x_off                  # locate first node in line
            if len(n) > 1:                                      # more nodes in line
                x_r = np.argmin(line[x-x_off+1:] != '0') + x+1  # find them
                y_r = y                                         
            else:                                               # no more nodes in line
                x_r = y_r = -1
            if y < (w_map.shape[0]-1):                          # not at end of map
                line_v = w_map[y+1:,x]                          # vertical line
                n_b = line_v[line_v == '0']                     # find bottom nodes
                if len(n_b) > 0:                                # found some nodes
                    y_b = np.argmin(line_v != '0') + y+1        # find first one
                    x_b = x
                else:                                           # no bottom node
                    x_b = y_b = -1
            else:                                               # no more lines
                    x_b = y_b = -1
            s_out += f"{x} {y} {x_r} {y_r} {x_b} {y_b}\n"       # add line to output
            chop = x_r-x_off if x_r > 0 else len(line)          # amount to chop from line
        else:                                                   # no nodes
            chop = len(line)                                    # chop the full line
        line = line[chop:]                                      # apply chop
        x_off += chop                                           # increment offset
       
print(s_out)
