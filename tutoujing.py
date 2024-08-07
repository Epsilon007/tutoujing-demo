# -*- coding: utf-8 -*-

'''
2024年7月9日22:54:02
初中物理动态圆形路线凸透镜成像规律示意图
'''

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure(num="动态圆形轨道凸透镜成像规律", figsize=(10, 5))
plt.rcParams["font.family"] = "FangSong"  # 支持中文显示


plt.xlim((-6,6)) # 给x轴刻度限定范围
plt.ylim((-3,3))
plt.xticks([-4, -2, 2, 4],
           [r'$2f$', r'$f$', r'$f$', r'$2f$'])
plt.yticks([-1, 1],
           [r'$r$', r'$r$'])

ax = plt.gca() # gca = 'get current axis'
ax.spines['right'].set_color('none') # 这里对图形四个边框（称脊梁,spines）进行设置：删除右边和上边的边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom') # 将x轴的位置定在下边的边框脊梁上
ax.yaxis.set_ticks_position('left') # 将y轴的位置定在左边的边框脊梁上
ax.spines['bottom'].set_position(('data', 0)) # 将下边的边框脊梁(此时即x轴)的原点位置设在y轴的'data'0处(即y轴的0刻度处)
ax.spines['left'].set_position(('data', 0))

# 圆形轨迹
x1 = -4
y1 = 0
r = 1

a = np.arange(x1-r,x1+r,0.0001)
print(a,len(a))
b = np.sqrt(np.power(r,2)-np.power((a-x1),2))+y1

plt.plot(a,b,color='k', linewidth=2.0, linestyle='-')
plt.plot(a,-b,color='k', linewidth=2.0, linestyle='-')

t_1 = 1
a0 = a[0]
b0 = np.sqrt(np.power(r,2)-np.power((a0-x1),2))+y1

x2 = np.linspace(a0, 6, 50)
y2 = (b0/a0)*x2
x3 = np.linspace(0, 6, 50)
y3 = b0-(b0/2)*x3

a0_sp4 = []
b0_sp4 = []
a0_sp4.append(a0)
b0_sp4.append(b0)
for i in range(len(a0_sp4)):
    plt.scatter(2 * a0_sp4[i] / (2 + a0_sp4[i]), 2 * b0_sp4[i] / (2 + a0_sp4[i]), s=50, c='r', marker='o')

spot1 = plt.scatter(a0,b0,s=45,c='r',marker='o')
spot2 = plt.scatter(0,b0,s=20,c='k',marker='o')
spot3 = plt.scatter(0,0,s=20,c='k',marker='o')
# spot4 = plt.scatter(2*a0/(2+a0),2*b0/(2+a0),s=50,c='r',marker='o')
line1, = ax.plot(x2,y2,'b--',lw=1.1)
line2, = ax.plot([a0,6],[b0,b0],'g--',lw=1.1)
line3, = ax.plot(x3,y3,'b--',lw=1.1)


def animate(n): # 这里n是指第n帧 这里定义的是下面'func'的更新方式
    plt.cla()

    plt.xlim((-6, 6))  # 给x轴刻度限定范围
    plt.ylim((-3, 3))
    plt.xticks([-4, -2, 2, 4],
               [r'$2f$', r'$f$', r'$f$', r'$2f$'])
    plt.yticks([-1, 1],
               [r'$r$', r'$r$'])

    ax = plt.gca()  # gca = 'get current axis'
    ax.spines['right'].set_color('none')  # 这里对图形四个边框（称脊梁,spines）进行设置：删除右边和上边的边框
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')  # 将x轴的位置定在下边的边框脊梁上
    ax.yaxis.set_ticks_position('left')  # 将y轴的位置定在左边的边框脊梁上
    ax.spines['bottom'].set_position(('data', 0))  # 将下边的边框脊梁(此时即x轴)的原点位置设在y轴的'data'0处(即y轴的0刻度处)
    ax.spines['left'].set_position(('data', 0))

    # 圆形轨迹
    x1 = -4
    y1 = 0
    r = 1

    a = np.arange(x1 - r, x1 + r, 0.0001)

    b = np.sqrt(np.power(r, 2) - np.power((a - x1), 2)) + y1

    plt.plot(a, b, color='k', linewidth=2.0, linestyle='-')
    plt.plot(a, -b, color='k', linewidth=2.0, linestyle='-')

    if n == 100:
        a0 = -3
        b0 = -(np.sqrt(np.power(r, 2) - np.power((a0 - x1), 2)) + y1)
    elif n > 100:
        t = 2
        a0 = a[(n - t*(n-100))*200]
        b0 = -(np.sqrt(np.power(r, 2) - np.power((a0 - x1), 2)) + y1)
    else:
        a0 = a[n*200]
        b0 = np.sqrt(np.power(r,2)-np.power((a0-x1),2))+y1
    print(n)

    a0_sp4.append(a0)
    b0_sp4.append(b0)
    # print(len(a0_sp4))

    for i in range(len(a0_sp4)):
        plt.scatter(2 * a0_sp4[i] / (2 + a0_sp4[i]), 2 * b0_sp4[i] / (2 + a0_sp4[i]), s=5, c='r', marker='o')

    x2 = np.linspace(a0, 6, 50)
    y2 = (b0/a0)*x2
    x3 = np.linspace(0, 6, 50)
    y3 = b0-(b0/2)*x3


    spot1 = plt.scatter(a0,b0,s=45,c='r',marker='o')
    spot2 = plt.scatter(0,b0,s=20,c='k',marker='o')
    spot3 = plt.scatter(0, 0, s=20, c='k', marker='o')
    spot4 = plt.scatter(2 * a0 / (2 + a0), 2 * b0 / (2 + a0), s=50, c='k', marker='o')
    line1, = ax.plot(x2,y2,'b--',lw=1.5)
    line2, = ax.plot([a0,6],[b0,b0],'g--',lw=1.5)
    line3, = ax.plot(x3,y3,'b--',lw=1.5)

    return a0

def init():
    a0 = a[0]
    return a0

'''
def trajectory(a0_1):
    b0_1 = np.sqrt(np.power(r, 2) - np.power((a0_1 - x1), 2)) + y1

    spot1 = plt.scatter(a0_1, b0_1, s=45, c='r', marker='o')
    spot2 = plt.scatter(0, b0_1, s=20, c='k', marker='o')
    spot3 = plt.scatter(0, 0, s=20, c='k', marker='o')
    spot4 = plt.scatter(2 * a0_1 / (2 + a0_1), 2 * b0_1 / (2 + a0_1), s=50, c='r', marker='o')

    return spot1, spot2, spot3, spot4


spot1, spot2, spot3, spot4 = trajectory(a0)
'''


# 这里参数'frames'设为100帧；频率'interval'为20毫秒更新一次；参数'blit'是指每次更新是否要更新整张图面的点(False)还是只更新那些变化了的点(True)
ani = animation.FuncAnimation(fig=fig, func=animate, frames=200, init_func=init, interval=1, blit=False)


plt.show()








