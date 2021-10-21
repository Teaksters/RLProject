from tqdm import tqdm as _tqdm
import numpy as np

def tqdm(*args, **kwargs):
    return _tqdm(*args, **kwargs, mininterval=1)  # Safety, do not overflow buffer


def q_learning(env, policy, Q, num_episodes, s_2_idx, discount_factor=1.0, alpha=0.5, max_epL=float('inf')):
    """
    Q-Learning algorithm: Off-policy TD control. Finds the optimal greedy policy
    while following an epsilon-greedy policy

    Args:
        env: OpenAI environment.
        policy: A behavior policy which allows us to sample actions with its sample_action method.
        Q: Q value function
        num_episodes: Number of episodes to run for.
        discount_factor: Gamma discount factor.
        alpha: TD learning rate.

    Returns:
        A tuple (Q, stats).
        Q is a numpy array Q[s,a] -> state-action value.
        stats is a list of tuples giving the episode lengths and returns.
    """

    # Keeps track of useful statistics
    stats = []

    for i_episode in tqdm(range(num_episodes)):
        i = 0
        R = 0

        # YOUR CODE HERE
        s = env.reset()

        done = False
        while done == False:
            a = policy.sample_action(s)
            s2, r, done, _ = env.step(a)
            if s_2_idx != None: # For blackJack
                Q[s_2_idx[s]][a] += alpha * (r + discount_factor * max(Q[s_2_idx[s2]]) - Q[s_2_idx[s]][a])
            else: # For others
                Q[s][a] += alpha * (r + discount_factor * max(Q[s2]) - Q[s][a])
            s = s2

            i += 1
            R += r
            if i == max_epL: break
        stats.append((i, R))
    episode_lengths, episode_returns = zip(*stats)
    return Q, (episode_lengths, episode_returns)
