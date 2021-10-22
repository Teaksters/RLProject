import matplotlib.pyplot as plt
import numpy as np
import pickle

# path = "pickle_files/Organized/"


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

                combinations.append([slippy, episodes, size, str(hole)])

    return combinations

def plot_all():
    combinations = loop_experiments()
    slippy_4_Q = []
    slippy_4_DQ = []
    noslippy_4_Q = []
    noslippy_4_DQ = []
    # slippy_8_Q = []
    # slippy_8_DQ = []
    # noslippy_8_Q = []
    # noslippy_8_DQ = []
    for i in range(len(combinations)):
        slippy, episodes, size, hole = combinations[i]
        # if slippy == "noslippy" and size == "8":
        if size == "8":
            continue
        mean_DQ, mean_Q = extract_pickle(slippy, episodes, size, hole)
        mean_DQ = np.mean(mean_DQ[-100:])
        mean_Q =  np.mean(mean_Q[-100:])
        if slippy == "slippy":
            if size == "4":
                # print("ja1")
                slippy_4_DQ.append(mean_DQ)
                slippy_4_Q.append(mean_Q)
            else:
                # print("ja2")
                pass
                # slippy_8_DQ.append(mean_DQ)
                # slippy_8_Q.append(mean_Q)
        else:
            if size == "4":
                # print("ja3")
                noslippy_4_DQ.append(mean_DQ)
                noslippy_4_Q.append(mean_Q)
            else:
                # print("ja4")
                pass
                # noslippy_8_DQ.append(mean_DQ)
                # noslippy_8_Q.append(mean_Q)

    print(slippy_4_Q)
    print(slippy_4_DQ)
    print(noslippy_4_Q)
    print(noslippy_4_DQ)
    plt.figure(1)
    plt.plot(slippy_4_Q, label="slippy_4_Q")
    plt.plot(slippy_4_DQ, label="slippy_4_DQ")
    plt.legend()
    plt.figure(2)
    plt.plot(noslippy_4_Q, label="noslippy_4_Q")
    plt.plot(noslippy_4_DQ, label="noslippy_4_DQ")
    # plt.plot(slippy_8_Q)
    # plt.plot(slippy_8_DQ)
    # plt.plot(noslippy_8_Q)
    # plt.plot(noslippy_8_DQ)
    plt.legend()
    plt.show()

plot_all()
