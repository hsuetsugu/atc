N = 3
S = 'ABFEKKSKEOWKF'

for s in S:
    temp = ord(s)+N
    if temp > ord('Z'):
        temp = ord('A') + temp - ord('Z') -1
    print(chr(temp), sep="", end="")
print()
