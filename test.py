import main

import numpy as np
import matplotlib.pyplot as plt
import pickle

pName = "Q_test_frozen_lake_50N_random.p"
# pName = "Q_test_cliff_walking.p"
N = 50
episodes = 500000
all_r = np.zeros([episodes])
all_r_dq = np.zeros([episodes])
for i in range(N):
    # _, (len, res) = main.main(env=2, num_episodes=episodes, epsilon=0.05, q=True, dq=False)
    # _, _, (len, res) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=False, dq=True)
    _, (len, res), _, _, (len, res_dq) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=True, dq=True)
    all_r += res
    all_r_dq += res_dq

mean_res = all_r / N
mean_res_dq = all_r_dq / N

pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))

# mean_res = pickle.load( open("pickle_files/" + pName, "rb" ))

# x = np.arange(mean_res.shape[0])
# plt.plot(x, mean_res)
# plt.show()
