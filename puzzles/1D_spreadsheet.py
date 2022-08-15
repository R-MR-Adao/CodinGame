import sys

def validate(a,s):
    if a != '_':
        if a[0]=='$':
            ind = int(a[1:])
            if ind < len(s): return str(s[ind])
            else: return 'ss[' + str(ind) + ']'
        else: return a
    else: return ''

def func(a,b,f,s):
    a = validate(a,s)
    b = validate(b,s)
    if f == 'VALUE': return a
    elif f == 'ADD': return a + '+' + b
    elif f == 'SUB': return a + '-' + b
    elif f == 'MULT': return a + '*' + b

n = int(input())
ss = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    ss.append('(' + func(arg_1, arg_2, operation,ss) + ')')

j = 0
while sum([1 for i in ss if type(i) == str]) > 0:
    if type(ss[j]) == str:
        try:
            res = eval(ss[j])
            if type(res) == int: ss[j] = res
        except: 1
    j += 1
    if j >= len(ss): j = 0
    
for i in range(n):
    print(ss[i])
