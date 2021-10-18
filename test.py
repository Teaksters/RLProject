import main

import numpy as np
import matplotlib.pyplot as plt
import pickle

all_r = []
for i in range(10):
    _, (len, res) = main.main(env=0, num_episodes=500000, epsilon=0.05,
                       q=True, dq=False)
    all_r.append(res)

mean_res = np.mean(all_r, axis=0)
pickle.dump(mean_res, open( "save.p", "wb" ))

mean_res = pickle.load( open( "save.p", "rb" ) )

x = np.arange(mean_res.shape[0])
plt.plot(x, mean_res)
plt.show()
