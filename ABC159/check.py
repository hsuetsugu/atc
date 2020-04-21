import numpy as np
import time

st = time.time()

for cnt in range(2 ** (10 - 1)):
    # bitで1の場所が切れ目とする
    option_h = np.array([int(s) for s in list(bin(cnt))[2:][::-1]])

print(f'{time.time()-st} sec')