# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
import pylab as plt
import numpy as np

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
plt.figure(figsize=(10,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
plt.subplot(1,1,1)

X = np.linspace(0, 5, 100,endpoint=False)
log_X = np.log(X)
nlog_X = -1*np.log(X)
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plt.plot(X, log_X, color="blue", linewidth=1, linestyle="-")
plt.plot(X, nlog_X, color="red", linewidth=1.5, linestyle=":")

# 设置横轴的上下限
xmin ,xmax = X.min(), X.max()
ymin, ymax = log_X.min(), log_X.max()

dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2

plt.xlim(xmin - dx, xmax + dx)
plt.ylim(ymin - dy, ymax + dy)


# 设置横轴记号
plt.xticks([-0.5, 0, 1, 2, 3, 4],
       [r'$-0.5$', r'$0$', r'$1$', r'$+2$', r'$3$', r'$4$'])

plt.yticks([-2, 0, +2],
       [r'$-2$', r'$0$', r'$+2$'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.legend(loc='upper left')
# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
plt.show()