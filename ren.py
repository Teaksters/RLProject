from run_experiment import run_experiment_func
import pickle

# Config A
pName       = ""
N           = 10
episodes    = 500000
size        = 4
p           = 0.8

pName = "FrozenLake_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_p" + str(int(p * 10)) + ".p"

mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, p)
pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))

print("***************")
print("*CONFIG A DONE*")
print("***************")

# Config B
pName       = ""
N           = 10
episodes    = 500000
size        = 8
p           = 0.9

pName = "FrozenLake_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_p" + str(int(p * 10)) + ".p"

mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, p)
pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
