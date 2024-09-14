import numpy as np

coords = np.array([input().split() for i in range(int(input()))]        # building coordinates
                   ).astype(int)

len_x = np.ptp(coords[:,0])                                             # length of x component
len_y = sum(abs(coords[:,1] - np.median(coords[:,1])))                  # length of y component

print(int(len_x + len_y))                                               # total cabling length
