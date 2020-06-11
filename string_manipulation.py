N = 3
S = 'ABFEKKSKEOWKF'

for s in S:
    temp = ord(s)+N
    if temp > ord('Z'):
        temp = ord('A') + temp - ord('Z') -1
    print(chr(temp), sep="", end="")
print()

# 文字列比較
# ABC141-E
def check3(m):
    # これはOK(pypyではなくpython3）
    dic = defaultdict(str)
    # dic = {}
    for i in range(n-m+1):
        s_ = s[i:i+m]
        if s_ in dic.keys():
            if dic[s_]+m<=i:
                return True
        else:
            dic[s_] = i
    return False


# 文字列比較（ローリングハッシュ）
# ABC141-E
# ただし，sは[数値]
# s = list(map(ord, list(input()[:-1])))

mod = 10**9+7
base = 1234
power = [1]*(n+1)
for i in range(1, n+1):
    power[i] = power[i-1]*base%mod

def check2(m):
    res = 0
    for i in range(m):
        res+=s[i]*power[m-i-1]
        res%=mod

    dic = {res: 0}
    # defaultdictが早い
    # dic = defaultdict(int)
    # dic[res] = 0

    for i in range(n-m):
        res = ((res-s[i]*power[m-1])*base+s[i+m]) % mod
        if res in dic.keys():
            index = dic[res]
            if index +m<=i+1:
                return True
        else:
            dic[res] = i+1
    return False