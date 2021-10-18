import main

import numpy as np
import matplotlib.pyplot as plt
import pickle

pName = "Q_test_cliff_walking.p"
N = 5
episodes = 300000
all_r = np.zeros([episodes])
for i in range(N):
    _, (len, res) = main.main(env=2, num_episodes=episodes, epsilon=0.05, q=True, dq=False)
    # _, _, (len, res) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=False, dq=True)
    # _, (len, res), _, _, (len, res) = main.main(env=0, num_episodes=episodes, epsilon=0.05, q=True, dq=True)
    all_r += res

mean_res = all_r / N
print(mean_res)
pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))

mean_res = pickle.load( open("pickle_files/" + pName, "rb" ))

x = np.arange(mean_res.shape[0])
plt.plot(x, mean_res)
plt.show()
