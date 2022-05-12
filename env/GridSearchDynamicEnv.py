# In this environment,
# Algorithm: D* (Dynamic A* Search)

# Different from the GridSearchEnv, we modified the follow things:

# 1. neighbors lists:
# neighbors : all the 4 direction of the current node

import numpy as np
import collections
import heapq

np.random.seed(4);

class Env():
    def __init__(self, height, width):
        super(Env, self).__init__()
        self.action_name = ['up', 'down', 'left', 'right']
        self.action_space = [0, 1, 2, 3]
        self.height = height
        self.width = width
        self.p = 0.8  ## the nums of human percentage in the map
        # self.map = np.zeros([height, width])

        # TODOLIST: if human <= 2 we need to random this map again, to ensure the reward can converge...
        self.map = np.random.choice(a=[0, 1], size=(self.height, self.width), p=[self.p, 1 - self.p])
        self.cost_map = np.random.randint(low = 1, high = 10,size = (self.height, self.width))

        self.position = [self.height - 1, 0]
        self.walls = np.array(self.matrix2Coordinate()) ## [[1,2], [1,3]]
        self.position_walls = list(zip(self.walls.T[0], self.walls.T[1])) ## [(1,2), (1,3)]

    def neighbors(self, position):
        (x, y) = position
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bound, neighbors)
        # results = filter(self.passable, results) 和静态环境描述不同，这里暂时不对墙壁进行过滤
        # 这段代码返回的是迭代器类型的数据，如果想要显示结果，还需要变成List（result）
        return results

    def cost(self, position, next_position):
        # donot use current position
        x_next = next_position[0]
        y_next = next_position[1]
        if position == next_position:
            return 0
        return self.cost_map[x_next][y_next]

    def in_bound(self, position):
        x = position[0]
        y = position[1]
        return 0 <= x <= self.height - 1 and 0 <= y <= self.width - 1

    def passable(self, position):
        x = position[0]
        y = position[1]
        return (x, y) not in self.position_walls


    def render(self):
        ## 这里还应该去除上一个时刻的状态
        render_map = np.copy(self.map)
        x = self.position[0]
        y = self.position[1]
        real_position = self.map[x][y]
        print("     EGO Position:", x, y)
        if (real_position == 1):
            ## print("x = ", x, "y = ", y)
            render_map[x][y] = 3
        else:
            render_map[x][y] = 2
        print(render_map)
        return render_map

    def matrix2Coordinate(self):
        ## find the 1 in the map and convert them to coordinate
        ## [h, w] --> [[x0,y0],[x1,y1]...]
        coordinate = []
        for i in range(self.height):
            for j in range(self.width):
                if self.map[i][j] == 1:
                    coordinate.append([i, j])
        return coordinate


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        ## 这里做了一点点修改，我们希望同时返回坐标和k值， 注意：k是最小的h值
        return heapq.heappop(self.elements)[1], heapq.heappop(self.elements)[0]