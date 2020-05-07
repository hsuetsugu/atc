from collections import defaultdict

# case1: keyの存在確認なしにインクリメントできる（カウンターとして使いやすい）
word1 = "sasakama"
d = defaultdict(int)
for w in word1:
    d[w] += 1
print(d)

# case2: keyごとにリストを作成していく
s = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')]
dd = defaultdict(list)
for k, v in s:
    dd[k].append(v)
print(dd)
