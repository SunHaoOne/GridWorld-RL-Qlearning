import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        ## 这里做了一点点修改，我们希望同时返回坐标和k值
        return heapq.heappop(self.elements)[1], heapq.heappop(self.elements)[0]


open_list = {}
start = (0, 0)
open_list[start] = {'p':(1, 0), 't':"open", 'h':10,'k':10}
print(open_list[start])

# X的下一个节点是Y，b(X) = Y, Y的父节点是X

print("parent", open_list[start]['p'])
print("state:", open_list[start]['t'])
print("k:", open_list[start]['h'])
print("h:", open_list[start]['k'])

frontier = PriorityQueue()

positions = [(0, 0), (0, 1), (0, 2), (1, 1)]
values = [5, 3, 4, 5]

## 这样操作完后，最小的节点是（0，1）的坐标，然后进一步处理后可以得到一下结果



for i in range(len(values)):
    # 根据这个k值进行排序
    frontier.put(positions[i], values[i])
    open_list[positions[i]] = {'p':(2,2),'t':"open", 'h':0,'k':0}
    # cost_so_far[positions[i]]['t'] = "open"
    # cost_so_far[positions[i]]['h'] = 10
    # cost_so_far[positions[i]]['k'] = 10


## 定义两个结构来存储结果，一个是openlist，用来维护位置和k值，另一个是dict，用来存储每个点的其他信息，如状态，h和k值

def min_state(frontier, open_list):
    ## 找到最小的节点后将其pop掉
    ## 这里还应该添加一个操作，将open_list里的k值和地址加入进这个优先队列中
    for key in open_list.keys():
        frontier.put(key, open_list[key]['k'])

    if frontier.empty():
        print("Open_List is NULL")
        return None
    state, k = frontier.get()
    if (open_list[start]['t'] == "open"):
        open_list[state]['t'] = "close"
    return state, k

from env.GridSearchDynamicEnv import Env

env = Env(10, 10)

def modify_cost(state, neighbor, env, open_list):
    if open_list[state]['t'] == "close":
        insert_node(state, neighbor, env)


def modify(state, neighbor, env, open_list):
    modify_cost(state, neighbor, env, open_list)
    while True:
        _, k_min = process_state()
        if open_list[state]['h'] < k_min:
            break

def insert_node(state, neighbor, open_list, env):
    ## 初始化的时候，所有的状态应该为new
    # https://blog.csdn.net/banzhuan133/article/details/100532206?spm=1001.2101.3001.6650.1
    t = open_list[state]['t']
    h_new = open_list[neighbor]['h'] + env.cost(state, neighbor)

    if t == "new":
        open_list[state]['k'] = h_new
    elif t == "open":
        open_list[state]['k'] = min(open_list[state]['k'], h_new)

    elif t == "close":
        # 这个条件是当新的障碍物出现的时候。针对已规划的cost发生变化的状态
        open_list[state]['k'] = min(open_list[state]['k'], h_new)
        open_list[state]['h'] = h_new
        open_list[state]['t'] = "open"


def process_state(frontier, open_list):
    current, k_old = min_state(frontier, open_list)
    if state is None:
        return -1
    ## 找到最小的值，并且将他们移除

    if k_old < open_list[current]['h']:
        for next in env.neighbors(current):
            if k_old >= open_list[next]['h'] and open_list[current]['h'] > open_list[next]['h'] + env.cost(current, next):

                open_list[current]['p'] = next
                open_list[current]['h'] = open_list[next]['h'] + env.cost(current, next)

    if k_old == open_list[current]['h']:
        for next in env.neighbors(current):
            if open_list[next]['t'] == "new" or \
                    open_list[next]['p'] == current and open_list[next]['h'] != open_list[current]['h'] + env.cost(current, next) or \
                    open_list[next]['p'] != current and open_list[next]['h'] > open_list[current]['h'] + env.cost(current, next) and next != (9, 9):

                open_list[next]['p'] = current
                insert_node(next, current)

    else:
        for next in env.neighbors(current):
            if open_list[next]['t'] == "new" or \
                    open_list[next]['p'] == current and open_list[next]['h'] != open_list[current]['h'] + env.cost(current, next):

                open_list[next]['p'] = current
                insert_node(next, current)
            else:
                if open_list[next]['p'] == current and open_list[next]['h'] > open_list[current]['h'] + env.cost(current, next):

                    insert_node(current, current)
                else:

                    if open_list[next]['p'] != current and \
                        open_list[current]['h'] > open_list[next]['h'] + env.cost(current, next) and \
                        open_list[next]['t'] == "close" and \
                        open_list[next]['h'] > k_old:
                        insert_node(next, next)

    return min_state(frontier, open_list)

state, k = min_state(frontier, open_list)

print("min_state:", state)
print("min_k_value:", k)

print(open_list)


## 可以定义y的parent是x， 如果在寻找的过程中发现了这个X->Y->Goal


## 这样在设置环境的过程中，neighbors不过滤这个墙的边界