# import numpy
import numpy as np

from Algorithms.Qlearner import q_learning
from Algorithms.double_Q import double_q_learning
from Policies.policy import EpsilonGreedyPolicy
from Envs.frozen_lake import FrozenLakeEnv
from Envs.blackjack import BlackjackEnv
from Envs.cliffwalking import CliffWalkingEnv
from Envs.taxi import TaxiEnv

import helpers


# Standard variables
env_opt = ['frozenLake', 'blackJack', 'cliffWalking', 'taxi']
env = 0
policy = 0
epsilon = 0.01
num_episodes = 500000


def main():

    s_2_idx = None
    env_choice = env_opt[0] # Change this to change the env
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

    if env_choice == 'cliffWalking':
        env = CliffWalkingEnv()
        Q = np.zeros((env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        print('The generated map:')
        env.render()

    if env_choice == 'taxi':
        env = TaxiEnv()
        Q = np.zeros((env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        print('The generated map:')
        env.render()

    # Q1, Q2, results = double_q_learning(env, policy, Q, num_episodes, s_2_idx,
    #                         discount_factor=0.9, alpha=0.5)
    # print(Q1, Q2)
    Q, results = q_learning(env, policy, Q, num_episodes, s_2_idx,
                            discount_factor=0.9, alpha=0.5)
    print("Q", Q)
    print("results", results)
    helpers.result_plot_forzen_lake(results[0], results[1])




if __name__=="__main__":
    main()
