import main

import numpy as np
import matplotlib.pyplot as plt
import pickle


def run_experiment_func(pName, N, episodes, size, p):
    pName = "Q_test_frozen_lake_50N_random.p"

    all_r = np.zeros([episodes])
    all_r_dq = np.zeros([episodes])

    for i in range(N):
        print(i)
        _, (len, res), _, _, (len_dq, res_dq) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=True, dq=True, size=size, p=p)
        all_r += res
        all_r_dq += res_dq

    mean_res = all_r / N
    mean_res_dq = all_r_dq / N
    # print("pickle_files/" + pName)
    # print("pickle_files/D" + pName)
    return mean_res, mean_res_dq
