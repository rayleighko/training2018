import numpy as np
import matplotlib.pylab as plt
def basic_softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def simple_softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

x = np.array([800, 695, 690])
y1 = basic_softmax(x) # nan 출력(값을 초과함)
y2 = simple_softmax(x) # 상대적으로 작은 값, 값 간의 차이를 줄이기 위한 방법 - 각 값을 해당 array의 최대값으로 뺀 값

plt.plot(x, y1)
plt.plot(x, y2, linestyle="--")
plt.ylim(-0.1, 1.1)

print(y1)
print(y2)
print(np.sum(y1)) # 값의 합은 언제나 1이다.
print(np.sum(y2)) # 값의 합은 언제나 1이다.

plt.show()