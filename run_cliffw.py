import main2

import numpy as np
import matplotlib.pyplot as plt
import pickle


def run_experiment_func(pName, N, episodes, size=4, number_holes=2):
    all_r = np.zeros([episodes])
    all_r_dq = np.zeros([episodes])

    for i in range(N):
        _, (len, res), _, _, (len_dq, res_dq) = main2.main(env=2, num_episodes=episodes, epsilon=0.05, q=True, dq=True, size=size, number_holes=number_holes, max_epL=100)
        all_r += res
        all_r_dq += res_dq

    mean_res = all_r / N
    mean_res_dq = all_r_dq / N
    return mean_res, mean_res_dq

pName = "Q_test_cliff_walking_100N_zeros.p"
q, dq = run_experiment_func(pName, 50, 20000)

pickle.dump(q, open("pickle_files/" + pName, "wb" ))
pickle.dump(dq, open("pickle_files/D" + pName, "wb" ))
