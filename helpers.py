def blackJack_s2idx_dict():
    s2idx = dict()
    idx = 0
    for i in range(12, 32):
        for j in range(1, 11):
            for k in [False, True]:
                s2idx[(i, j, k)] = idx
                idx += 1
    return s2idx
