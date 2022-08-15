import sys
import math

message = input()

ascii_message = ''.join([format(ord(c),'b') if str.isalpha(c) else '0'+format(ord(c),'b') for c in message])
s = ''
i = 0
while i < len(ascii_message):
    c =  ascii_message[i]
    try: n = min([ii for ii,cc in enumerate(ascii_message[i:]) if cc != c])
    except: n = len(ascii_message[i:])
    if c == '0': s += '0'
    s += '0 ' + n*'0' + ' '
    i = i + n
print(s[:-1])
