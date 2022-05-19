import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

MAP_COLORS = {
    0: (142, 207, 201),
    1: (255, 190, 122),
    2: (250, 127, 111),
    3: (130, 176, 210),
}
MAP_LABELS = ["UP","Down", "Left", "Right"]
MAP_SPACE = [key for key in MAP_COLORS]
# MAP_SPACE = [0, 1, 2, 3]

def get_patches(colors, labels = ["UP","Down", "Left", "Right"]):
    patches = []
    for i in range(len(colors)):
        patches.append(mpatches.Patch(color=colors[i], label=labels[i]))
    return patches
def convert2matplotlib_cmap(colors = MAP_COLORS):
    cmap_colors = []
    for color in colors:
        r = colors[color][0] / 255.0
        g = colors[color][1] / 255.0
        b = colors[color][2] / 255.0
        alpha = 1.0
        cmap_colors.append((r, g, b, alpha))
    return cmap_colors
def vis_matrix(matrix, map_space=MAP_SPACE):
    # visualize the matrix with the MAP_COLORS
    # (h, w) -> (h, w, 3)
    canvas = np.zeros(matrix.shape + (3,), dtype=np.uint8)
    for choice in map_space:
        canvas[matrix == choice] = MAP_COLORS[choice]
    print(canvas)
    return canvas


if __name__=="__main__":

    # Case 1: matrix shape : (h, w, 3)
    ax1 = plt.subplot(2, 2, 1)

    matrix_2D = np.random.randint(low=0, high=4, size=(5, 5))
    matrix_3D = vis_matrix(matrix_2D)
    plt.imshow(matrix_3D)
    cmap_colors = convert2matplotlib_cmap(colors=MAP_COLORS)
    patches = get_patches(cmap_colors, labels=MAP_LABELS)
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('3D Matrix')


    # Case 2: matrix shape: (h, w, 1)
    ax2 = plt.subplot(2, 2, 2)

    matrix_2D = 10 * np.random.rand(5, 5)
    matrix_2D_image = plt.imshow(matrix_2D, cmap='viridis')
    plt.colorbar(matrix_2D_image, fraction=0.046, pad=0.04)
    plt.title('2D Matrix')

    plt.show()