# import main
#
# import numpy as np
# import matplotlib.pyplot as plt
# import pickle
#
# pName = "Q_test_frozen_lake_8x8_test.p"
# # pName = "Q_test_cliff_walking.p"
# N = 1
# episodes = 100000
# all_r = np.zeros([episodes])
# all_r_dq = np.zeros([episodes])
# for i in range(N):
#     # _, (len, res) = main.main(env=2, num_episodes=episodes, epsilon=0.05, q=True, dq=False)
#     # _, _, (len, res) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=False, dq=True)
#     _, (len, res), _, _, (len, res_dq) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=True, dq=True)
#     all_r += res
#     all_r_dq += res_dq
#
# mean_res = all_r / N
# mean_res_dq = all_r_dq / N
#
# pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
# pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
#
# # mean_res = pickle.load( open("pickle_files/" + pName, "rb" ))
#
# # x = np.arange(mean_res.shape[0])
# # plt.plot(x, mean_res)
# # plt.show()

from run_experiment import run_experiment_func
import pickle

# Config A
pName           = ""
N               = 100
episodes        = 50000
size            = 8
number_holes    = 25

pName = "FrozenLake_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_holes" + str(number_holes) + ".p"

mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, number_holes)
pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
