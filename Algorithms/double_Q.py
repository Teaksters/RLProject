from tqdm import tqdm as _tqdm
# import numpy
import numpy as np
import random

def tqdm(*args, **kwargs):
    return _tqdm(*args, **kwargs, mininterval=1)  # Safety, do not overflow buffer


def double_q_learning(env, policy1, policy2, Q1, Q2, num_episodes, s_2_idx, discount_factor=1.0, alpha=0.5):
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
            # Sample from mean epsilon greedy policies
            mean_action_value = Q1[s] + Q2[s]

            x = random.random()
            if x > policy1.epsilon:
                a = np.argmax(mean_action_value)
            else:
                a = random.randint(0, policy1.nA - 1)


            s2, r, done, _ = env.step(a)
            if s_2_idx != None: # For blackJack
                if np.random.choice([0, 1], 1) == 1:
                    Q1[s_2_idx[s]][a] += alpha * (r + discount_factor * Q2[np.argmax(Q1[s_2_idx[s2]])][a] - Q1[s_2_idx[s]][a])
                else:
                    Q2[s_2_idx[s]][a] += alpha * (r + discount_factor * Q1[np.argmax(Q2[s_2_idx[s2]])][a] - Q2[s_2_idx[s]][a])
            else: # For others
                if np.random.choice([0, 1], 1) == 1:
                    Q1[s][a] += alpha * (r + discount_factor * Q2[s2][np.argmax(Q1[s2])] - Q1[s][a])
                else:
                    Q2[s][a] += alpha * (r + discount_factor * Q1[s2][np.argmax(Q2[s2])] - Q2[s][a])
            s = s2

            i += 1
            R += r

        stats.append((i, R))
    episode_lengths, episode_returns = zip(*stats)
    return Q1, Q2, (episode_lengths, episode_returns)
