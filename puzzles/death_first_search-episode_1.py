import sys
import math

n, l, e = [int(i) for i in input().split()]
links = [ [] for _ in range(n) ]  # list of links
gates = []  # list of gateways
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links[n1].append(n2)
    links[n2].append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    eib = [i for i in gates if i in links[si]]
    print(eib, file=sys.stderr, flush=True)
    if len(eib) == 0:
        ei = gates[0]
    else:
        ei = eib[0]
    li = links[ei]
    d0 = ei
    if ei in links[si]:
        d1 = si        
    else:
        d1 = li[0]
    links[d0].remove(d1)
    links[d1].remove(d0)
    if len(links[ei]) == 0:
        gates.remove(ei)
    print("{} {}".format(d0,d1))
