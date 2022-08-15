import sys, math

def printf(s):                                  # debug print
    print(s, file=sys.stderr, flush=True)

w = 19                                          # map width
h = 25                                          # map height
mp = [["{}"for i in range(w)]for i in range(h)] # initialize map
insts = input().split()                         # instructions
printf(insts)                                   # print instructions

for inst in insts:
    op = "MOW"                                  # operation mode
    if inst[0:8] == "PLANTMOW":                 # check if PLANTMOW
        op = "PLANTMOW"
        inst = inst[8:]
    elif inst[0:5] == "PLANT":                  # check if PLANT
        op = "PLANT"
        inst = inst[5:]
    x = ord(inst[0])-ord("a")                   # center x
    y = ord(inst[1])-ord("a")                   # center y
    d = int(inst[2:])                           # diameter
    for xx in range(w):                         # iterate x
        for yy in range(h):                     # iterate y
            if math.sqrt((xx - x)**2 + (yy - y)**2) <= d/2: # point in radius
                if   op == "MOW"  : mp[yy][xx] = "  "
                elif op == "PLANT": mp[yy][xx] = "{}"
                else              : mp[yy][xx] = "{}" if mp[yy][xx] == "  " else "  "
                    
for i in range(h):                              # print the map
    print(''.join(mp[i]))

