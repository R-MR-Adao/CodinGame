# define constants
START = [4, 8]                                                          # starting position
ROWS, COLS = 9, 17                                                      # board dimensions

# define functions 
def run(board, fingerprint):
    """ run game """

    # definitions
    offset = [                                                          # offset options
        [-1,-1],                                                        # up-left    (↖ North West)
        [-1, 1],                                                        # up-right   (↗ North East)
        [1 ,-1],                                                        # down-left  (↙ South West)
        [1 , 1]                                                         # down-right (↘ South East)
    ]
    
    move = lambda p, o, M: min([M - 1, max([0, p + o])])                # func update position

    # run path
    y, x = START                                                        # current position

    for pair in fingerprint.split(':'):                                 # iterate over keys
        for hex_key in pair[::-1]:                                      # reverse iterate over pair
            key = int(hex_key,16)                                       # convert to bin
            for step in [key & 3, key >> 2]:                            # isolate steps to follow
                off = offset[step]                                      # position offset
                y = move(y, off[0], ROWS)                               # y position
                x = move(x, off[1], COLS)                               # x position
                board[y][x] += 1                                        # update counter
    
    return y, x                                                         # return end position

def build_string(board, end):
    """ convert board to string """

    # definitions
    chars = " .o+=*BOX@%&#/^"                                           # chars list
    S =    lambda r, c: (r == START[0] and c == START[1])               # check if on start position
    E =    lambda r, c: (r == end[0] and c == end[1])                   # check if on end position
    n2c =  lambda v   : chars[v % len(chars)]                           # number to char
    v2c =  lambda r, c, v: 'S' if S(r,c) else 'E' if E(r,c) else n2c(v) # values to char
    line = lambda r,ro: [v2c(r, c, v) for c,v in enumerate(ro)]         # build line

    # build string
    bs = ["+---[CODINGAME]---+"]                                        # header
    bs += [f"|{''.join(line(r,ro))}|" for r, ro in enumerate(board)]    # iterate over rows
    bs += ["+-----------------+"]                                       # footer
    return bs

# define chess board
board = [[0]*COLS for _ in range(ROWS)]                                 # chess board

# game start
fingerprint = input()                                                   # input string
end = run(board, fingerprint)                                           # run path
board_str = build_string(board, end)                                    # string board

# output results
for row in board_str:                                                   # iterate over rows
    print(row)                                                          # print row
