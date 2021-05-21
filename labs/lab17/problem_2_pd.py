import numpy as np

path_to_A, path_to_b = input(), input()
X = np.array(list(map(float, input().split())))

with open(path_to_A) as file_A:
    A = np.array([list(map(float, row.split())) for row in file_A.readlines()])

with open(path_to_b) as file_b:
    b = np.array(list(map(float, file_b.read().split())))

print(((A.dot(A)).dot(X)).dot(b))