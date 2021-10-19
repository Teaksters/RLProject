import pickle
import numpy as np
import matplotlib.pyplot as plt

# mean_DQ = pickle.load( open("pickle_files/DQ_test_frozen_lake.p", "rb" ))
mean_Q = pickle.load( open("pickle_files/Q_test_frozen_lake.p", "rb" ))
print(mean_Q)

# x = np.arange(mean_DQ.shape[0])
# plt.plot(x, mean_DQ)
# plt.savefig("owyeah_DQ")
# plt.show()

x = np.arange(0, mean_Q.shape[0], 10000)
plt.scatter(x, mean_Q[::10000])
plt.savefig("pickle_plots/Q_test_frozen_lake.png")
plt.show()
