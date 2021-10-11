import numpy as np

from Algorithms.Qlearner import q_learning
from Envs.frozen_lake import FrozenLakeEnv
from Policies.policy import EpsilonGreedyPolicy


# Standard variables
env_opt = ['frozen']
env = 0
policy = 0
epsilon = 0.1
num_episodes = 15


def main():
    env_choice = env_opt[0]
    if env_choice == 'frozen':
        env = FrozenLakeEnv(desc=None, map_name="4x4", is_slippery=True)
        Q = np.zeros((env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon)
    Q, results = q_learning(env, policy, Q, num_episodes,
                            discount_factor=1.0, alpha=0.5)
    # print(Q, results)




if __name__=="__main__":
    main()
