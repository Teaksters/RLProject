import pickle
import numpy as np
import matplotlib.pyplot as plt

# mean_DQ = pickle.load( open("pickle_files/Arn/cliffwalking/DQ_test_cliff_walking_100N_random.p", "rb" ))
# mean_Q = pickle.load( open("pickle_files/Arn/cliffwalking/Q_test_cliff_walking_100N_random.p", "rb" ))

mean_DQ = pickle.load( open("pickle_files/Arn/cliffwalking/DQ_test_cliff_walking_100N_zeros.p", "rb" ))
mean_Q = pickle.load( open("pickle_files/Arn/cliffwalking/Q_test_cliff_walking_100N_zeros.p", "rb" ))
print(mean_Q)

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

print(len(y_Q))
x = np.arange(1, len(y_DQ) + 1) * STEP
print(x, y_Q)
plt.plot(x, y_Q, color="r", alpha=0.5, label = "Q-learning")
plt.plot(x, y_DQ, color="b", alpha=0.5, label = "Double Q-learning")
plt.title('Cliffwalking with Uniform zeros initialization')
plt.xlabel('Number of Episodes')
plt.ylabel('Average Score (N=100)')
plt.legend()
plt.show()

# x = np.arange(0, mean_Q.shape[0], 10000)
# plt.scatter(x, mean_Q[::10000])
# plt.savefig("pickle_plots/Q_test_frozen_lake.png")
# plt.show()
