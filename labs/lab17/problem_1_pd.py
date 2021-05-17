import numpy as np
import pandas as pd

n, m = input().split()
n = int(n)
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data_frame = pd.DataFrame(data)
print(np.sum((data_frame < -5).sum(axis=1)))
print(int(abs(np.sum(data_frame[(data_frame < 0)].sum()))))
print(int(max(data_frame[(data_frame > 0)].max())))