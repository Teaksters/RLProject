import matplotlib.pyplot as plt
import numpy as np
import pickle


def extract_pickle(slippy, episodes, size, holes):
    mean_DQ = pickle.load(open("pickle_files/Organized/" + "DFrozenLake_" + slippy + "_N100_epi" + episodes + "_size" + size + "_holes" + holes + ".p", "rb"))
    mean_Q  = pickle.load(open("pickle_files/Organized/" + "FrozenLake_"  + slippy + "_N100_epi" + episodes + "_size" + size + "_holes" + holes + ".p", "rb"))

    return mean_DQ, mean_Q

def loop_experiments():
    slippys = ["slippy", "noslippy"]
    sizes = ["4", "8"]
    holes = 8

    combinations = []

    for slippy in slippys:
        for size in sizes:
            for hole in range(1, holes + 1):
                if size == "4" and slippy == "slippy" and hole < 5:
                    episodes = "10000"
                elif size == "8" and slippy == "slippy":
                    episodes = "20000"
                else:
                    episodes = "50000"

                if slippy == "noslippy" and size == "8" and hole > 6:
                    continue
                combinations.append([slippy, episodes, size, str(hole)])

    return combinations

def plot_all():
    combinations = loop_experiments()
    slippy_4_Q = []
    slippy_4_DQ = []
    noslippy_4_Q = []
    noslippy_4_DQ = []
    slippy_8_Q = []
    slippy_8_DQ = []
    noslippy_8_Q = []
    noslippy_8_DQ = []
    for i in range(len(combinations)):
        slippy, episodes, size, hole = combinations[i]
        mean_DQ, mean_Q = extract_pickle(slippy, episodes, size, hole)
        mean_DQ = np.mean(mean_DQ[-100:])
        mean_Q =  np.mean(mean_Q[-100:])
        if slippy == "slippy":
            if size == "4":
                slippy_4_DQ.append(mean_DQ)
                slippy_4_Q.append(mean_Q)
            else:
                slippy_8_DQ.append(mean_DQ)
                slippy_8_Q.append(mean_Q)
        else:
            if size == "4":
                noslippy_4_DQ.append(mean_DQ)
                noslippy_4_Q.append(mean_Q)
            else:
                noslippy_8_DQ.append(mean_DQ)
                noslippy_8_Q.append(mean_Q)

    x = np.arange(1, 9)
    plt.figure(1)
    plt.plot(x, slippy_4_Q, c="red", label="Q-learning")
    plt.plot(x, slippy_4_DQ, c="blue", label="DQ-learning")
    plt.legend()
    plt.savefig("slippy_4")
    plt.figure(2)
    plt.plot(x, noslippy_4_Q, c="red", label="Q-learning")
    plt.plot(x, noslippy_4_DQ, c="blue", label="DQ-learning")
    plt.legend()
    plt.savefig("noslippy_4")
    plt.figure(3)
    plt.plot(x, slippy_8_Q, c="red", label="Q-learning")
    plt.plot(x, slippy_8_DQ, c="blue", label="DQ-learning")
    plt.legend()
    plt.savefig("slippy_8")
    plt.figure(4)
    plt.plot(x[:-2], noslippy_8_Q, c="red", label="Q-learning")
    plt.plot(x[:-2], noslippy_8_DQ, c="blue", label="DQ-learning")
    plt.legend()
    plt.savefig("noslippy_8")
    plt.show()

plot_all()

combinations = loop_experiments()

# import os
# print("TODO")
# for combination in combinations:
#     slippy, episodes, size, holes = combination
#     dq = "pickle_files/Organized/" + "DFrozenLake_" + slippy + "_N100_epi" + episodes + "_size" + size + "_holes" + holes + ".p"
#     q =  "pickle_files/Organized/" + "FrozenLake_" + slippy + "_N100_epi" + episodes + "_size" + size + "_holes" + holes + ".p"
#     if not os.path.isfile(dq):
#         print(combination)
#
#     else:
#         plt.figure()
#         mean_DQ, mean_Q = extract_pickle(slippy, episodes, size, holes)
#
#         STEP = 20
#
#         y_Q = []
#         episode_mean_Q = []
#         for i in range(len(mean_Q)):
#             episode_mean_Q.append(mean_Q[i])
#             if i % STEP == 0:
#                 y_Q.append(sum(episode_mean_Q) / len(episode_mean_Q))
#                 episode_mean_Q = []
#
#         y_DQ = []
#         episode_mean_DQ = []
#         for i in range(len(mean_DQ)):
#             episode_mean_DQ.append(mean_DQ[i])
#             if i % STEP == 0:
#                 y_DQ.append(sum(episode_mean_DQ) / len(episode_mean_DQ))
#                 episode_mean_DQ = []
#
#         # print(len(y_Q))
#         x_Q = np.arange(1, len(y_Q) + 1) * STEP
#         x_DQ = np.arange(1, len(y_DQ) + 1) * STEP
#
#         plt.scatter(x_Q, y_Q, color="r", alpha=0.5, label = "Q-learning")
#         plt.scatter(x_DQ, y_DQ, color="b", alpha=0.5, label = "Double Q-learning")
#         plt.legend()
#         plt.savefig("preliminary_plots/" + size + "_" + holes + "_" + slippy)
