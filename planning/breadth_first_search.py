from env.GridSearchEnv import Env, Queue
import numpy as np
import matplotlib.pyplot as plt
from vis_q_table import get_patches, convert2matplotlib_cmap
## refer to https://www.redblobgames.com/pathfinding/a-star/introduction.html

def breadth_first_search(env, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for next in env.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return came_from



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


def get_route_map(map, parents, start, goal):
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

    return route_map, final_route_map

def visualize_result(map, parents, start, goal):
    route_map, final_route_map = get_route_map(map, parents, start, goal)
    route_map = vis_q_map(route_map)
    final_route_map = vis_q_map(final_route_map)
    ax1 = plt.subplot(1, 2, 1)
    plt.imshow(route_map)
    plt.title('Search Area')

    ax2 = plt.subplot(1, 2, 2)
    plt.imshow(final_route_map)
    cmap_colors = convert2matplotlib_cmap(colors=ACTION_COLORS)
    patches = get_patches(cmap_colors, labels=ACTION_LABELS)
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('Search Route')

    plt.savefig("../img/breath_first_search.png", bbox_inches = 'tight')
    plt.show()

# beautiful visualize methods....

# map 0
# obstacle color 1
# route color 2
# start color 3
# end color 4

ACTION_COLORS = {
    0: (0, 0, 0),
    1: (142, 207, 201),
    2: (255, 190, 122),
    3: (250, 127, 111),
    4: (130, 176, 210),
}
ACTION_LABELS = ["Map", "Wall","Route", "Start", "End"]
ACTION_SPACE = [key for key in ACTION_COLORS]

def vis_q_map(q_map, action_space=ACTION_SPACE):
    # visualize the q_map with the ACTION_COLORS
    # (h, w) -> (h, w, 3)
    canvas = np.zeros(q_map.shape + (3,), dtype=np.uint8)
    for action in action_space:
        canvas[q_map == action] = ACTION_COLORS[action]
    return canvas



if __name__ == "__main__":


    HEIGHT = 10
    WIDTH = 10
    GOAL = (8, 8)
    START = (0, 0)

    env = Env(HEIGHT, WIDTH)
    env.render()
    env.p = 0.99

    parents = breadth_first_search(env = env, start=START, goal=GOAL)

    # visualize_searching(map = env.map, parents = parents)
    visualize_result(map = env.map, parents = parents, start = START, goal = GOAL)
