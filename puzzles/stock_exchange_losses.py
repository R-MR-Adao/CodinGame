# functions

reset = lambda i: (vs[i], float('inf'), vs[i])              # valley start, min and max
get_max_loss = lambda: min(loss, local_min - valley_start)  # calculate maximum loss

# globals

n = int(input())                                            # total number of values
vs = [int(i) for i in input().split()]                      # list of values

valley_start, local_min, local_max = reset(0)               # valley start, min and max                  
loss = 0                                                    # the target

# begin search

for i in range(1, n):                                       # iterate over range of values
    if vs[i] < local_max:                                   # still in same valley
        local_min = min(local_min, vs[i])                   # update local minimum
    else:                                                   # new valley
        loss = get_max_loss()                               # update maximum loss
        valley_start, local_min, local_max = reset(i)       # reset aux local_min

print(get_max_loss())                                       # print result
