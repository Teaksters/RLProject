import numpy as np

from Algorithms.Qlearner import q_learning
from Policies.policy import EpsilonGreedyPolicy
from Envs.frozen_lake import FrozenLakeEnv
from Envs.blackjack import BlackjackEnv
import helpers


# Standard variables
env_opt = ['frozenLake', 'blackJack']
env = 0
policy = 0
epsilon = 0.1
num_episodes = 10000
s_2_idx = None


def main():
    env_choice = env_opt[1]
    if env_choice == 'frozenLake':
        env = FrozenLakeEnv(desc=None, map_name="4x4", is_slippery=True)
        Q = np.zeros((env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        print('The generated map:')
        env.render()

    if env_choice == 'blackJack':
        env = BlackjackEnv()
        s = env.reset()
        s_2_idx = helpers.blackJack_s2idx_dict()
        Q = np.zeros((env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA, s_2_idx)

    Q, results = q_learning(env, policy, Q, num_episodes, s_2_idx,
                            discount_factor=0.9, alpha=0.5)
    print(Q)




if __name__=="__main__":
    main()
