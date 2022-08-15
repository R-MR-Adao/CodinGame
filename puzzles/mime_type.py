import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeDic = {}
fnames = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeDic[ext.lower()] = mt
for i in range(q):
    fnames.append(input())  # One file name per line.
print(mimeDic, file=sys.stderr, flush=True)
print(fnames, file=sys.stderr, flush=True)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for f in fnames:
    print('file = {}'.format(f), file=sys.stderr, flush=True)
    fname = f.split('.')
    if (len(fname) > 1) and (fname != ''):
        ext = fname[-1]
        print('fname = {}, ext = {}'.format(fname,ext), file=sys.stderr, flush=True)
        try:
            s = mimeDic[ext.lower()]
        except:
            s = "UNKNOWN"
    else:
        s = "UNKNOWN"
    print(s)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

