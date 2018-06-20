# Multi-Layer Perceptron for solve XOR problem.
# 왜냐하면 하나의 레이어를 지닌 퍼셉트론에서는 선형 구조만 가능한데, 이러한 선형 구조는 XOR 문제에 적용할 수 없기 때문이다.
import numpy as np

# 가중치(weight)와 편향(bias) 도입 AND Perceptron
def AND(x1 ,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# Not AND Perceptron with weight, bias
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# OR Perceptron whith weight, bias
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 기존 게이트(AND, NAND, OR)를 조합해 XOR을 구현하는 방법 (X OR Y) AND (X NAND Y)
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# Use XOR Perceptron(Multi-Layer)
# x1과 x2를 가지고 0층에서 NAND와 OR를 수행하고, 나온 결과 s1과 s2를 이용해 1층에서 AND를 수행해 2층에서 결과 값 을 출력(y)
print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))

