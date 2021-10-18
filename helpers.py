import matplotlib.pyplot as plt
import numpy as np

def blackJack_s2idx_dict():
    s2idx = dict()
    idx = 0
    for i in range(12, 32):
        for j in range(1, 11):
            for k in [False, True]:
                s2idx[(i, j, k)] = idx
                idx += 1
    return s2idx

def result_plot_forzen_lake(episode_lengths, episode_returns):
    episode_number = np.arange(len(episode_lengths))
    x_red, y_red, x_green, y_green = [], [], [], []

    for i in range(len(episode_number)):
        if episode_returns[i] == 0:
            x_red.append(episode_number[i])
            y_red.append(episode_lengths[i])
        else:
            x_green.append(episode_number[i])
            y_green.append(episode_lengths[i])

    plt.scatter(x_red, y_red, color="r", label="Failed runs")
    plt.scatter(x_green, y_green, color="g", label="Successfull runs")
    plt.legend()
    plt.show()
