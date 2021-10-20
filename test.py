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

import numpy as np
import random

def generate_random_map(size=4, p=0.8):
    """Generates a random valid map (one that has a path from start to goal)
    :param size: size of each side of the grid
    :param p: probability that a tile is frozen
    """
    valid = False

    # DFS to check that it's a valid path.
    def is_valid(res):
        frontier, discovered = [], set()
        frontier.append((0, 0))
        while frontier:
            r, c = frontier.pop()
            if not (r, c) in discovered:
                discovered.add((r, c))
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for x, y in directions:
                    r_new = r + x
                    c_new = c + y
                    if r_new < 0 or r_new >= size or c_new < 0 or c_new >= size:
                        continue
                    if res[r_new][c_new] == "G":
                        return True
                    if res[r_new][c_new] != "H":
                        frontier.append((r_new, c_new))
        return False

    while not valid:
        p = min(1, p)
        res = np.random.choice(["F", "H"], (size, size), p=[p, 1 - p])
        res[0][0] = "S"
        res[-1][-1] = "G"
        valid = is_valid(res)
    return ["".join(x) for x in res]

print(generate_random_map(size=4, p=0.8))

def generate_random_map_new(size, number_holes):
    """Generates a random valid map (one that has a path from start to goal)
    :param size: size of each side of the grid
    :param p: probability that a tile is frozen
    """
    valid = False

    # DFS to check that it's a valid path.
    def is_valid(res):
        frontier, discovered = [], set()
        frontier.append((0, 0))
        while frontier:
            r, c = frontier.pop()
            if not (r, c) in discovered:
                discovered.add((r, c))
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for x, y in directions:
                    r_new = r + x
                    c_new = c + y
                    if r_new < 0 or r_new >= size or c_new < 0 or c_new >= size:
                        continue
                    if res[r_new][c_new] == "G":
                        return True
                    if res[r_new][c_new] != "H":
                        frontier.append((r_new, c_new))
        return False

    while not valid:
        res = np.full((size, size), "F")
        for i in range(number_holes):
            x_index = random.randint(0, size - 1)
            y_index = random.randint(0, size - 1)
            while (x_index == 0 and y_index == 0) or (x_index == size - 1 and y_index == size - 1):
                x_index = random.randint(0, size - 1)
                y_index = random.randint(0, size - 1)
            res[x_index][y_index] = "H"
        res[0][0] = "S"
        res[-1][-1] = "G"
        valid = is_valid(res)
    return ["".join(x) for x in res]

print(generate_random_map_new(8, 5))
