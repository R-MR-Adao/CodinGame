for i in range(int(input()))
    s = input()                                                         # input arrays
    varName = s.split('[')[0]                                           # variable name
    i0 = int(s[len(varName)+1].split('..')[0])                          # first index
    i1 = int(s[len(varName)+1].split('..')[1].split(']')[0])            # last index
    a = [int(i) for i in list(s.split('= ')[1].split(' '))]             # array data
    vars().__setitem__(varName, {i  a[i-i0] for i in range(i0,i1+1)})   # create new variable

print(eval(input()))                                                    # evaluate operation
