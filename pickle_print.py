import pickle
import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
mean_DQ = pickle.load( open("pickle_files/DFrozenLake_N100_epi50000_size4_holes4not_slippery.p", "rb" ))
mean_Q = pickle.load( open("pickle_files/FrozenLake_N100_epi50000_size4_holes4not_slippery.p", "rb" ))
=======
mean_DQ = pickle.load( open("pickle_files/DFrozenLake_noslippy_N100_epi50000_size8_holes1.p", "rb" ))
mean_Q = pickle.load( open("pickle_files/FrozenLake_noslippy_N100_epi50000_size8_holes1.p", "rb" ))
>>>>>>> 7fabcf70b52ceeab807414d38dbb6291ca16bc7c
print(mean_Q)

# x = np.arange(mean_DQ.shape[0])
# plt.plot(x, mean_DQ)
# plt.savefig("owyeah_DQ")
# plt.show()
STEP = 100

y_Q = []
episode_mean_Q = []
for i in range(len(mean_Q)):
    episode_mean_Q.append(mean_Q[i])
    if i % STEP == 0:
        y_Q.append(sum(episode_mean_Q) / len(episode_mean_Q))
        episode_mean_Q = []

y_DQ = []
episode_mean_DQ = []
for i in range(len(mean_DQ)):
    episode_mean_DQ.append(mean_DQ[i])
    if i % STEP == 0:
        y_DQ.append(sum(episode_mean_DQ) / len(episode_mean_DQ))
        episode_mean_DQ = []

# print(len(y_Q))
x = np.arange(1, len(y_DQ) + 1) * STEP
# print(x, y_Q)
plt.scatter(x, y_Q, color="r", alpha=0.5, label = "Q-learning")
plt.scatter(x, y_DQ, color="b", alpha=0.5, label = "Double Q-learning")
plt.legend()
plt.show()

# x = np.arange(0, mean_Q.shape[0], 10000)
# plt.scatter(x, mean_Q[::10000])
# plt.savefig("pickle_plots/Q_test_frozen_lake.png")
# plt.show()
