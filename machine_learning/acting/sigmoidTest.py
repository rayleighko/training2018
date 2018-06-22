import numpy as np
import matplotlib.pylab as plt

# sigmoid function used broadcast for numpy array.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

a = np.array([-1.0, 1.0, 2.0])

print(sigmoid(a))

# 이와 같은 시그모이드 함수를 그래프로 나타내 그 변화를 살펴보자.

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()

