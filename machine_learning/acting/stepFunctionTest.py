import numpy as np
import matplotlib.pylab as plt
# Don't use Numpy
def simple_step_function(x):
    if x > 0:
        return 1
    else:
        return 0

# possible use Numpy
def np_step_function(x):
    y = x > 0
    return y.astype(np.int)

def simple_np_step_finction(x):
    return np.array( x > 0, dtype = np.int)

a = 3.0
b = np.array([-1.0, 1.0, 2.0])

print(simple_step_function(a))
# simple_step_function(b) # Don't use this
# print(step_function(a)) # Don't use this
print(np_step_function(b))

# inside np_step_function
# y = b > 0
# print(y.astype(np.int))
# 여기서 print(y)와 print(astype(np.int))의 차이를 살펴보면 위와 같은 함수의 트릭을 이해할 수 있다.
# 첨언하자면 y에 b에 대한 bool 배열을 저장하고, 저장된 bool 배열을 int형으로 바꿔 반환한다.
# 이를 더 간편하게 한 simple_np_step_function을 사용해 그래프를 사용해보자.

x = np.arange(-5.0, 5.0, 0.1)
y = simple_np_step_finction(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()

# 0을 경계로 출력이 0에서 1로 바뀐다. 마치 계단처럼 말이다. 시그모이드 함수는 조금 더 부드럽다.