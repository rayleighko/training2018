import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('assets/lena.png')

plt.imshow(img)
plt.show()