import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as mpatches
x = np.arange(0,  3  * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1, third parameter is the sequence
#1 comes the first then is the second
# 1
ax=plt.subplot(2,  1,  1)
plt.plot(x, y_sin)
plt.title('Sine')
ax.annotate('local max', xy=(2,1), xytext=(3,1.5),arrowprops=dict(facecolor='black', shrink=0.05))
# 2
plt.subplot(2,  1,  2,facecolor=(0.1843,0.3098,0.3098))
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,polar=True,facecolor=(0.55686,0.8980392,0.93333))
theta=np.arange(0,2*np.pi,0.01)
ax1.plot(theta,5*(1-np.sin(theta)),lw=2,c='r')                         #参数：角度，半径，linestyle样式
#r=5*(1-np.sin(theta)
ax1.fill(theta,5*(1-np.sin(theta)),'r')
ax1.grid(False)
plt.show()



x=np.arange(-10,10,1)
y=2*x+3
plt.title("unofficial test zero", fontproperties='Times New Roman')
plt.xlabel("x axis", fontproperties='Times New Roman')
plt.ylabel("y axis", fontproperties='Times New Roman')
plt.plot(x, y)
plt.grid()
plt.show()
#this comes figure 2 which is a dot plot
plt.plot(x,y,"ob")#'ob'can have many shapes see figure in COO：）
plt.show()

fig = plt.figure()
ax1=fig.add_subplot(111)
x = np.arange(0,6, 0.1)
y=x+0.05
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax1.text(3, 5, "Sample A", ha="center", va="center", size=20,bbox=bbox_props)
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
ax1.text(2, 3, "Direction", ha="center", va="center", rotation=30,size=10,bbox=bbox_props)


plt.plot(x,y,'o',label='y=x+0.05')
plt.plot(x,y+1,'g',label='line graph')
ax1.legend(bbox_to_anchor=(0,1), loc='upper left', borderaxespad=1)
#there are four parameter in describing the position of graph
#(x,y) x 0=left 1=right y 1=upper 0=supper loc around which direction 4:d
plt.show()
#draw sine graph in math
#x = np.arange(0,  3  * np.pi,  0.1)
#y = np.sin(x)
#plt.title("sine wave form")
# 计算正弦和余弦曲线上的点的 x 和 y 坐标







