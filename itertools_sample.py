import itertools

ary = [1, 3, 5 ,6, 9]
cumsum = itertools.accumulate(ary)
print(list(cumsum))

# 順列組み合わせ
print('permutations')
print(list(itertools.permutations([1, 2, 3])))

# combination
print('combinations')
print(list(itertools.combinations([1, 2, 3], 2)))

# 重複あり組み合わせ
print('combinations with replacement')
print(list(itertools.combinations_with_replacement([1, 2, 3], 2)))