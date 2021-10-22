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
policy = 0

def main(env=0, num_episodes=50000, epsilon=0.05, q=True, dq=False, size=4, number_holes=2, max_epL=100):

    s_2_idx = None
    env_choice = env_opt[env] # Change this to change the env
    if env_choice == 'frozenLake':
        env = FrozenLakeEnv(desc=None, map_name=None, is_slippery=False, size=size, number_holes=number_holes)
        Q = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q1 = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q2 = np.random.normal(0, 0.01, (env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        policy2 = EpsilonGreedyPolicy(Q2, epsilon, env.nA)
        print('The generated map:')
        env.render()

    if env_choice == 'blackJack':
        env = BlackjackEnv()
        s = env.reset()
        s_2_idx = helpers.blackJack_s2idx_dict()
        Q = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q1 = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q2 = np.random.normal(0, 0.01, (env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA, s_2_idx)
        policy2 = EpsilonGreedyPolicy(Q2, epsilon, env.nA, s_2_idx)

    if env_choice == 'cliffWalking':
        env = CliffWalkingEnv()
        Q = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q1 = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q2 = np.random.normal(0, 0.01, (env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        policy2 = EpsilonGreedyPolicy(Q2, epsilon, env.nA)
        print('The generated map:')
        env.render()

    if env_choice == 'taxi':
        env = TaxiEnv()
        Q = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q1 = np.random.normal(0, 0.01, (env.nS, env.nA))
        Q2 = np.random.normal(0, 0.01, (env.nS, env.nA))
        policy = EpsilonGreedyPolicy(Q, epsilon, env.nA)
        policy2 = EpsilonGreedyPolicy(Q2, epsilon, env.nA)
        print('The generated map:')
        env.render()

    # Decide which algorithm to run
    if dq:
        Q1, Q2, dq_results = double_q_learning(env, policy, policy2, Q1, Q2, num_episodes, s_2_idx,
                                discount_factor=0.9, alpha=0.5, max_epL=200)
    if q:
        Q, q_results = q_learning(env, policy, Q, num_episodes, s_2_idx,
                                discount_factor=0.9, alpha=0.5, max_epL=200)

    if q and dq:
        return Q, q_results, Q1, Q2, dq_results
    elif q:
        return Q, q_results
    elif dq:
        return Q1, Q2, dq_results

    # Q, results = q_learning(env, policy, Q, num_episodes, s_2_idx,
    #                         discount_factor=0.9, alpha=0.5)
    # print("Q", Q)
    # print("results", results)
    # helpers.result_plot_forzen_lake(results[0], results[1])



if __name__=="__main__":
    main()
