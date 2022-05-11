import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# self.action_name = ['up', 'down', 'left', 'right']
# self.action_space = [0, 1, 2, 3]
ACTION_COLORS = {
    0: (142, 207, 201),
    1: (255, 190, 122),
    2: (250, 127, 111),
    3: (130, 176, 210),
}
ACTION_LABELS = ["UP","Down", "Left", "Right"]
ACTION_SPACE = [key for key in ACTION_COLORS]
# ACTION_SPACE = [0, 1, 2, 3]

# colors = [(142 / 255, 207 / 255, 201 / 255, 1.0),
#           (255 / 255, 190 / 255, 122 / 255, 1.0),
#           (250 / 255, 127 / 255, 111 / 255, 1.0),
#           (130 / 255, 176 / 255, 210 / 255, 1.0)]

def convert2matplotlib_cmap(colors = ACTION_COLORS):
    cmap_colors = []
    for color in colors:
        r = colors[color][0] / 255.0
        g = colors[color][1] / 255.0
        b = colors[color][2] / 255.0
        alpha = 1.0
        cmap_colors.append((r, g, b, alpha))
    return cmap_colors


def get_patches(colors, labels = ACTION_LABELS):
    patches = []
    for i in range(len(colors)):
        patches.append(mpatches.Patch(color=colors[i], label=labels[i]))
    return patches


def get_action_idx(q_table, colunm, x, y):
    state_idx = colunm * x + y
    action_idx = np.argmax(q_table[state_idx])
    return action_idx


def get_state_value(q_table, colunm, x, y):
    state_idx = colunm * x + y
    # V = max(Q(s,a))
    state_value = np.max(q_table[state_idx])
    return state_value


def get_q_map(map, q_table):
    render_map = np.copy(map)
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            action_idx = get_action_idx(q_table, map.shape[1], i, j)
            render_map[i][j] = action_idx
    return render_map


def vis_q_map(q_map, action_space=ACTION_SPACE):
    # visualize the q_map with the ACTION_COLORS
    # (h, w) -> (h, w, 3)
    canvas = np.zeros(q_map.shape + (3,), dtype=np.uint8)
    for action in action_space:
        canvas[q_map == action] = ACTION_COLORS[action]
    return canvas


def get_v_map(map, q_table):
    render_map = np.copy(map)
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            state_value = get_state_value(q_table, map.shape[1], i, j)
            render_map[i][j] = state_value
    return render_map

def get_route_map(map, route, idx):
    render_route_map = np.zeros_like(map)
    for i in range(len(route[idx])):
        x = route[idx][i][0]
        y = route[idx][i][1]
        render_route_map[x][y] = 1

    render_route_map[route[idx][0][0]][route[idx][0][1]] = 2
    render_route_map[route[idx][len(route[idx])-1][0]][route[idx][len(route[idx])-1][1]] = 3

    return render_route_map



if __name__ == "__main__":

    map = np.load('result/map.npy')
    q_table = np.load('result/q_table.npy')
    route = np.load('result/route_test.npy', allow_pickle=True)

    q_map = get_q_map(map, q_table)
    v_map = get_v_map(map, q_table)
    IDX = np.random.randint(len(route) - 1)
    render_route_map = get_route_map(map, route, idx = IDX)

    ax1 = plt.subplot(2, 2, 1)
    plt.imshow(map, cmap='gray')
    plt.title('MAP')

    ax2 = plt.subplot(2, 2, 2)
    # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    v_image = plt.imshow(v_map, cmap='viridis')
    plt.colorbar(v_image, fraction=0.046, pad=0.04)
    plt.title('V_MAP')

    ax3 = plt.subplot(2, 2, 3)
    plt.imshow(vis_q_map(q_map))
    cmap_colors = convert2matplotlib_cmap(colors=ACTION_COLORS)
    patches = get_patches(cmap_colors, labels=ACTION_LABELS)
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('Q_MAP')


    # ax4 = plt.subplot(2, 2, 4)
    # plt.imshow(render_route_map)
    # plt.title('ROUTE')

    plt.show()

