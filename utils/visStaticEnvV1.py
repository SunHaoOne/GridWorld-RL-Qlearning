import pygame as pg  # 命名为pg
import numpy as np
import sys
import random
from env.GridStaticEnv import Env
from algorithm.QLearning import Q_learning


def cal_pos(position):  # 得到实际尺度对应的可视化尺度
    m = position[0] * pixel / height
    n = position[1] * pixel / width
    radius_fake = radius * pixel / height
    pos_fake = [m, n]
    return pos_fake, radius_fake

height = 20
width = 20
radius = 5
env = Env(height, width, radius=radius)
epsilon = 0.1
episode = 20
pixel = 500

pg.init()  # 初始化pygame，并检查pygame包是否完整
pg.display.set_caption("可视化")  # 命名

screen = pg.display.set_mode((pixel, pixel), pg.SRCALPHA)  # 创建新的Surface对象，图形显示与此(宽高)，即像素
clock = pg.time.Clock()  # 设置帧率
colors = np.array([[255, 255, 255], [100, 149, 237], [173, 255, 47], [128, 0, 128]])  # 将列表转化为数组


done = False
running = True
state = env.reset()
while running:
    for event in pg.event.get():  # 监视键盘和鼠标事件
        if event.type == pg.QUIT:
            pg.display.quit()
            pg.quit()  # 与init（）相反，pg.QUIT会使pygame停止运行
            sys.exit()  # 终止程序
    for i in range(episode):  # 如果事件不是quit就执行移动程序
        env.reset()  # 重置UAV的位置
        gridarray = env.render()  # 输出带UAV的地图
        rewards = []
        surface = pg.surfarray.make_surface(colors[gridarray])

        while not done:

            action = np.random.choice([0, 1, 2, 3])  # 第一步随机探索
            action = env.getLegalAction(action)
            gridarray = env.render()
            surface = pg.surfarray.make_surface(colors[gridarray])
            surface = pg.transform.scale(surface, (pixel, pixel))
            screen.fill((192, 192, 192))
            screen.blit(surface, (0, 0))
            current_state = env.get_state()
            pos_fake, radius_fake = cal_pos(current_state)
            pg.draw.circle(screen, (255, 97, 0, 0), pos_fake, radius_fake, width=2)

            pg.display.flip()

            next_state, reward, done = env.step(action)

            clock.tick(500)  # 设置帧率
            pg.time.delay(800)
        done = False
    running = False
