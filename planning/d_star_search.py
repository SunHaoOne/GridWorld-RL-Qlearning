#!/usr/bin python
# coding:utf-8
import math
from sys import maxsize

# ————————————————
# 原文链接：https: // blog.csdn.net / qq_36458461 / article / details / 106106254

class State(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.state = "."
        self.t = "new"
        self.h = 0
        self.k = 0

    def cost(self, state):
        if self.state == "#" or state.state == "#":
            return maxsize
        return math.sqrt(pow(self.x - state.x, 2) + pow(self.y - state.y, 2))

    def set_state(self, state):
        if state not in [".", "@", "#", "+", "S", "E"]:
            return
        self.state = state


class Map(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = self.init_map()

    def init_map(self):
        map_list = []
        for i in range(self.row):
            temp = []
            for j in range(self.col):
                temp.append(State(i, j))
            map_list.append(temp)
        return map_list

    def print_map(self):
        for i in range(self.row):
            str_temp = ""
            for j in range(self.col):
                str_temp += self.map[i][j].state + " "
            print(str_temp)

    def get_neighbors(self, state):
        state_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if state.x + i < 0 or state.x + i >= self.row:
                    continue
                if state.y + j < 0 or state.y + j >= self.col:
                    continue
                state_list.append(self.map[state.x + i][state.y + j])
        return state_list

    def set_obstacle(self, point_list):
        for i, j in point_list:
            if i < 0 or i >= self.row or j < 0 or j >= self.col:
                continue
            self.map[i][j].set_state("#")


class DStar(object):
    def __init__(self, maps):
        self.map = maps
        self.open_list = set()

    def process_state(self):
        # print("In process_state")
        x = self.min_state()
        if x is None:
            return -1

        old_k = self.min_k_value()
        self.remove(x)

        if old_k < x.h:
            for y in self.map.get_neighbors(x):
                if old_k >= y.h and x.h > y.h + x.cost(y):
                    x.parent = y
                    x.h = y.h + x.cost(y)

        elif old_k == x.h:
            for y in self.map.get_neighbors(x):
                if (y.t == "new" or y.parent == x and y.h != x.h + x.cost(y) or y.parent != x and y.h > x.h + x.cost(
                        y)) and y != end:
                    y.parent = x
                    self.insert_node(y, x.h + x.cost(y))
        else:
            for y in self.map.get_neighbors(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y):
                    y.parent = x
                    self.insert_node(y, x.h + x.cost(y))
                else:
                    if y.parent != x and y.h > x.h + x.cost(y):
                        self.insert_node(x, x.h)
                    else:
                        if y.parent != x and x.h > y.h + x.cost(y) and y.t == "close" and y.h > old_k:
                            self.insert_node(y, y.h)

        return self.min_k_value()

    def min_state(self):
        if not self.open_list:
            print("Open_list is NULL")
            return None
        return min(self.open_list, key=lambda x: x.k)  # 获取openlist中k值最小对应的节点

    def min_k_value(self):
        if not self.open_list:
            return -1
        return min([x.k for x in self.open_list])  # 获取openlist表中值最小的k

    def insert_node(self, state, h_new):
        if state.t == "new":
            state.k = h_new
        elif state.t == "open":
            state.k = min(state.k, h_new)
        elif state.t == "close":
            state.k = min(state.k, h_new)
        state.h = h_new
        state.t = "open"
        self.open_list.add(state)

    def remove(self, state):
        if state.t == "open":
            state.t = "close"

        self.open_list.remove(state)

    def modify_cost(self, state):
        if state.t == "close":
            self.insert_node(state, state.parent.h + state.cost(state.parent))

    def modify(self, state):  # 当障碍物发生变化时，从目标点往起始点回推，更新由于障碍物发生变化而引起的路径代价的变化
        self.modify_cost(state)
        while True:
            k_min = self.process_state()
            if state.h <= k_min:
                break

    def run(self, start, end):
        # self.open_list.add(end)
        self.insert_node(end, 0)
        while True:
            self.process_state()
            if start.t == "close":
                break
        start.set_state("S")
        s = start
        while s != end:
            s = s.parent
            s.set_state("+")
        s.set_state("E")

        print("Before obstacle change!")
        self.map.print_map()

        temp_s = start

        self.map.set_obstacle([(12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11)])  # 障碍物发生变化

        while temp_s != end:
            temp_s.set_state("@")
            if temp_s.parent.state == "#":
                self.modify(temp_s)
                continue

            temp_s = temp_s.parent

        temp_s.set_state("E")

        print("After obstacle change!")
        self.map.print_map()


if __name__ == "__main__":
    mh = Map(25, 25)
    mh.set_obstacle([(6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (7, 4), (7, 5), (7, 6)])

    start = mh.map[3][2]
    end = mh.map[23][16]
    mh.print_map()

    dstar = DStar(mh)
    dstar.run(start, end)
