# 행렬의 내적
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A.shape)
print(B.shape)

print(np.dot(A, B)) # 내적을 구하는 함수

C = np.array([[12, 13, 14], [15, 16, 17]])
D = np.array([[20, 21], [22, 23], [24, 25]])

print(C.shape)
print(D.shape)

print(np.dot(C, D))

# 이제 간단한 신경망 구조를 만들어보자.
# (1 3 5)
# (2 4 6)
# 입력(X)과 위의 행렬을 곱해 각각 Y1과 Y2에 전달하는 것이다.

X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])

print(X.shape)
print(W.shape)

Y = np.dot(X, W)
print(Y)