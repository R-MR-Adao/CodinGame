from math import floor

n = int(input())

memo = [0 for i in range(n)]

def findTotal(first, last):
    dist = last-first
    if dist <= 3: return 0
    mid = floor((first+last)/2)
    memo[dist] = memo[dist] if memo[dist] else findTotal(first, mid) + findTotal(mid, last) + 1
    return memo[dist]

answer = [2, 1] if n == 4 or n == 3 else [1, 1]

i = 0
while (n > 4 and i <= floor(n/2)):
    total = (memo[i] if memo[i] else findTotal(0, i)) + (memo[n-1-i] if memo[n-1-i] else findTotal(i, n-1)) + (3 if i > 1 else 2)
    if (answer[0] < total):
        answer = [total, i+1]
    i += 1
print("{} {}".format(answer[0], answer[1]))