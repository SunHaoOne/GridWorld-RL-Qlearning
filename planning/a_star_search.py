from env.GridSearchEnv import Env, PriorityQueue
import numpy as np
import matplotlib.pyplot as plt


## A start算法的写法和dijkstar非常类似，只不过修改了这恶鬼代价函数

def heuristic(location_a, location_b):
    (x1, y1) = location_a
    (x2, y2) = location_b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(env, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in env.neighbors(current):
            new_cost = cost_so_far[current] + env.cost(current, next);
            if next not in came_from or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far


def get_distance_map(cost_so_far):
    distance_map = np.zeros_like(env.map)
    for key in cost_so_far.keys():
        x = key[0]
        y = key[1]
        distance_map[x][y] = cost_so_far[key];
    return distance_map;

def visualize_searching(map, parents):
    route_map = np.copy(map);
    for keys in parents.keys():
        x = keys[0]
        y = keys[1]
        route_map[x][y] = 2
        plt.imshow(route_map)
        plt.pause(0.01)
    route = []
    last_point = GOAL
    while True:
        # keys: end point, values, start point
        route.append(last_point)
        last_point = parents[last_point]
        if (last_point == START):
            route.append(last_point)
            break
    print(route)
    final_route_map = np.copy(env.map);
    for i in range(len(route)):
        x = route[i][0];
        y = route[i][1];
        final_route_map[x][y] = 2;
        plt.imshow(final_route_map);
        plt.pause(0.01)
    plt.show()

def visulize_result(map, parents, cost, start, goal):
    route_map = np.copy(map);
    for keys in parents.keys():
        x = keys[0]
        y = keys[1]
        route_map[x][y] = 2
    route = []
    last_point = GOAL
    while True:
        # keys: end point, values, start point
        route.append(last_point)
        last_point = parents[last_point]
        if (last_point == START):
            route.append(last_point)
            break

    final_route_map = np.copy(env.map);
    for i in range(len(route)):
        x = route[i][0];
        y = route[i][1];
        final_route_map[x][y] = 2;

    # ADD THE START AND GOAL POINT TO THE RENDER MAP
    route_map[start[0]][start[1]] = 3;
    final_route_map[start[0]][start[1]] = 3;

    route_map[goal[0]][goal[1]] = 4;
    final_route_map[goal[0]][goal[1]] = 4;

    ax1 = plt.subplot(1, 3, 1)
    plt.imshow(route_map)
    plt.title('Search Area')

    ax2 = plt.subplot(1, 3, 2)
    plt.imshow(final_route_map)
    plt.title('Search Route')

    ax3 = plt.subplot(1, 3, 3)
    distance_map = get_distance_map(cost)
    print("Cost Map:", distance_map)
    distance_image = plt.imshow(distance_map);
    plt.colorbar(distance_image, fraction=0.046, pad=0.04)
    plt.title('Cost Map')
    plt.show()

## 后续修改的时候注意搜索的函数需要传入env这个参数

if __name__ == "__main__":

    HEIGHT = 10
    WIDTH = 10
    GOAL = (9, 9)
    START = (0, 0)

    env = Env(HEIGHT, WIDTH)
    env.render()
    print(env.cost_map)
    env.p = 0.99

    parents, cost = a_star_search(env = env, start=START, goal=GOAL)
    print(parents)
    print(cost)

    visualize_searching(map = env.map, parents = parents)

    # visulize_result(map = env.map, parents = parents, cost = cost, start = START, goal = GOAL)

