import matplotlib.pyplot as plt
import numpy as np


def get_step_reward(avg_reward, step):
    step_reward = [0]
    for i in range(len(avg_reward)):
        if i % step == 0:
            step_reward.append(sum(avg_reward[i:i + step - 1]) / step)
    x = np.linspace(0, len(avg_reward), int(len(avg_reward) / step) + 1)
    return x, step_reward


def get_weighted_moving_reward(avg_reward, weight):
    # x = np.linspace(0, len(avg_reward) - 1, len(avg_reward))
    return np.convolve(avg_reward, np.ones(weight), 'same') / weight


def plot_reward(avg_reward):
    plt.figure()

    x, step_avg_reward = get_step_reward(avg_reward, step=10)
    plt.plot(x, step_avg_reward, 'r-', linewidth=3, alpha=0.3)

    x, step_avg_reward = get_step_reward(avg_reward, step=20)
    plt.plot(x, step_avg_reward, 'r-', linewidth=1.5, alpha=0.7)

    x, step_avg_reward = get_step_reward(avg_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)

    plt.plot(x, step_avg_reward, 'b-', linewidth=3, alpha=0.3)
    plt.plot(x, weighted_moving_reward, 'b-', linewidth=3, alpha=0.7)

    plt.show()


def plot_reward(train_reward, test_reward):
    plt.figure()

    ax1 = plt.subplot(1, 2, 1)
    plt.title('train')
    x, step_avg_reward = get_step_reward(train_reward, step=10)
    plt.plot(x, step_avg_reward, 'r-', linewidth=3, alpha=0.3)
    x, step_avg_reward = get_step_reward(train_reward, step=20)
    plt.plot(x, step_avg_reward, 'r-', linewidth=1.5, alpha=0.7)
    x, step_avg_reward = get_step_reward(train_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)
    plt.plot(x, step_avg_reward, 'b-', linewidth=3, alpha=0.3)
    plt.plot(x, weighted_moving_reward, 'b-', linewidth=3, alpha=0.7)

    ax2 = plt.subplot(1, 2, 2)
    plt.title('test')
    x, step_avg_reward = get_step_reward(test_reward, step=10)
    plt.plot(x, step_avg_reward, 'r-', linewidth=3, alpha=0.3)
    x, step_avg_reward = get_step_reward(test_reward, step=20)
    plt.plot(x, step_avg_reward, 'r-', linewidth=1.5, alpha=0.7)
    x, step_avg_reward = get_step_reward(test_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)
    plt.plot(x, step_avg_reward, 'b-', linewidth=3, alpha=0.3)
    plt.plot(x, weighted_moving_reward, 'b-', linewidth=3, alpha=0.7)

    plt.show()

def plot_reward2(train_reward, test_reward):
    plt.figure()

    x, step_avg_reward = get_step_reward(train_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)
    plt.plot(x, step_avg_reward, 'b-', linewidth=1.5, alpha=0.3, label = 'train_step_avg_reward')
    plt.plot(x, weighted_moving_reward, 'b-', linewidth=3, alpha=0.7, label = 'train_weighted_moving_reward')

    x, step_avg_reward = get_step_reward(test_reward, step=50)
    weighted_moving_reward = get_weighted_moving_reward(step_avg_reward, weight=2)
    plt.plot(x, step_avg_reward, 'r-', linewidth=1.5, alpha=0.3, label = 'test_step_avg_reward')
    plt.plot(x, weighted_moving_reward, 'r-', linewidth=3, alpha=0.7, label = 'test_weighted_moving_reward')

    plt.legend()
    plt.show()

if __name__ == "__main__":
    # CHOICES = ['train', 'test']

    train_reward = np.load('result/reward_train.npy')
    test_reward = np.load('result/reward_test.npy')

    # plot_reward(train_reward)
    # plot_reward(train_reward, test_reward)
    plot_reward2(train_reward, test_reward)

