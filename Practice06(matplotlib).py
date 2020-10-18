import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
lena = mpimg.imread('01.jpg')
lena.shape
plt.imshow(lena)
plt.axis('off')
plt.show()
print('Hello world')
import time
time.sleep(3)
lena = mpimg.imread('E:/01.jpg',1)
lena.shape
plt.imshow(lena)
plt.axis('off')
plt.show()


