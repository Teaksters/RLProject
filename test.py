import main

import numpy as np
import matplotlib.pyplot as plt
import pickle

pName = "save.p"
N = 50
episodes = 300000
all_r = np.zeros([episodes])
for i in range(N):
    _, (len, res) = main.main(env=0, num_episodes=episodes, epsilon=0.05,
                       q=True, dq=False)
    all_r += res

mean_res = all_r / N
print(mean_res)
pickle.dump(mean_res, open(pName, "wb" ))

mean_res = pickle.load( open(pName, "rb" ) )

x = np.arange(mean_res.shape[0])
plt.plot(x, mean_res)
plt.show()
