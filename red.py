from run_experiment import run_experiment_func
import pickle

# Config A
pName           = ""
N               = 100
episodes        = 20000
size            = 8
number_holes    = 7

pName = "FrozenLake_slippy_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_holes" + str(number_holes) + ".p"

mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, number_holes)
pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))

# print("***************")
# print("*CONFIG A DONE*")
# print("***************")
#
# # Config B
# pName       = ""
# N           = 100
# episodes    = 50000
# size        = 4
# number_holes           = 6
#
# pName = "FrozenLake_slippy_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_holes" + str(number_holes) + ".p"
#
# mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, number_holes)
# pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
# pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
#
# print("***************")
# print("*CONFIG A DONE*")
# print("***************")
#
# # Config B
# pName       = ""
# N           = 100
# episodes    = 50000
# size        = 4
# number_holes           = 7
#
# pName = "FrozenLake_slippy_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_holes" + str(number_holes) + ".p"
#
# mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, number_holes)
# pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
# pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
#
# print("***************")
# print("*CONFIG A DONE*")
# print("***************")
#
# # Config B
# pName       = ""
# N           = 100
# episodes    = 50000
# size        = 4
# number_holes           = 8
#
# pName = "FrozenLake_slippy_N" + str(N) + "_epi" + str(episodes) + "_size" + str(size) + "_holes" + str(number_holes) + ".p"
#
# mean_res, mean_res_dq = run_experiment_func(pName, N, episodes, size, number_holes)
# pickle.dump(mean_res, open("pickle_files/" + pName, "wb" ))
# pickle.dump(mean_res_dq, open("pickle_files/D" + pName, "wb" ))
#
# print("***************")
# print("*CONFIG A DONE*")
# print("***************")
