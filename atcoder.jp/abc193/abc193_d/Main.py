K = int(input())
S, T = [input() for _ in range(2)]

deck = [0] + [K for _ in range(9)]
h_s, h_t = [[0] + [0 for _ in range(9)] for _ in range(2)]
for si in S[:4]:
    deck[int(si)] -= 1
    h_s[int(si)] += 1
for ti in T[:4]: 
    deck[int(ti)] -= 1
    h_t[int(ti)] += 1

cnt = 0
for si in range(1, 9 + 1):
    if deck[si] == 0: continue

    cs = deck[si]
    deck[si] -= 1
    h_s[si] += 1
    p_s = sum([i * 10**h_s[i] for i in range(1, 9 + 1)])

    for ti in range(1, 9 + 1):
        if deck[ti] == 0: continue

        ct = deck[ti]
        h_t[ti] += 1
        p_t = sum([i * 10**h_t[i] for i in range(1, 9 + 1)])

        if p_s > p_t: cnt += cs*ct

        h_t[ti] -= 1
    
    deck[si] += 1
    h_s[si] -= 1

ans = cnt / ((9*K - 8)*(9*K - 9))

print(ans)