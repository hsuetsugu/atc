
# 26進数（ABC171 C問題）
n = int(input())

n -= 1
ans = []

while True:
    if n >= 26:
        ans.append(chr(ord('a') + (n % 26)))
        n = n // 26 -1
    else:
        ans.append(chr(ord('a') + (n % 26)))
        break

print(''.join(ans[::-1]))
