def check(s):
    for i,c in enumerate(s):
        cc = c
        while cc > 90: cc -= 26
        while cc < 65: cc += 26
        s[i] = cc
    return s

def inc(message,rot):
    message = check(message)
    for i in range(3):
        message = [ord(rot[i][chr(c)]) for c in message]
        message = check(message)    
    return message

operation = input()
n = int(input())
rote = []
rotd = []
for i in range(3):
    rotor = input()
    rote.append({chr(i+65):rotor[i] for i in range(len(rotor))})
    rotd.append({rotor[i]:chr(i+65) for i in range(len(rotor))})
rotd = [rotd[2-i] for i in range(3)]
message = input()

if operation == "ENCODE":
    message = [ord(c)+n+i for i,c in enumerate(message)]
    message = inc(message,rote)
if operation == "DECODE":
    message = [ord(c) for c in message]
    message = inc(message,rotd)
    message = [c-n-i for i,c in enumerate(message)]
    message = check(message)
print("".join([chr(c) for c in message]))
