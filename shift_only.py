N = 4
input = '5 6 8 10'
a_s = input.split()

cnt = 0
while True:
    a_s = [int(a) / 2 for a in a_s if int(a) % 2 == 0]
    if len(a_s) < N:
        break
    cnt += 1
print(cnt)
