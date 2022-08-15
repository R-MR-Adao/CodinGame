import sys
import math

def interpLine(line,i,dic):
    for ii in range(0,len(line),l):
        key = round(ii/l)
        linepart = line[ii:ii+l]
        if i == 0:
            dic[key] = [linepart]
        else:
            dic[key].append(linepart)
    return dic

def findNumber(v,s):
    n = 0
    for ii in range(0,len(v),l):
        order = s/l - ii/l - 1
        num = v[ii:ii+l]
        numn = next(key for key, value in nums.items() if value == num)
        n += numn * 20 ** order
    return n

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def formatNumber(n,l):
    num = numberToBase(n,20)
    print("num base 20 = {}".format(num), file=sys.stderr, flush=True)
    sout = []
    for n in num:
        sout += nums[n]
    return sout

l, h = [int(i) for i in input().split()]
nums = {}
n1 = {}
n2 = {}

for i in range(h):
    nums = interpLine(input(),i,nums)

s1 = int(input())
for i in range(s1):
    n1 = interpLine(input(),i,n1)

s2 = int(input())
for i in range(s2):
    n2 = interpLine(input(),i,n2)

operation = input()

# find number in nums
n1n = findNumber(n1[0],s1)
n2n = findNumber(n2[0],s2)
# express the command in a string
com = "{} {} {}".format(n1n,operation,n2n)
result = eval(com)
out = formatNumber(result,l)
for o in out:
    print(o)
