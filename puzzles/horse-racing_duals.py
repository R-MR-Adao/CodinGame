import sys
import math
from numpy import diff

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
p = [int(input()) for i in range(n)]
# Write an answer using print
p.sort()
print(min(diff(p)))