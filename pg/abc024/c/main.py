N, D, K = map(int, input().split())
LR = [list(map(lambda x: int(x), input().split())) for _ in range(D)]
ST = [list(map(lambda x: int(x), input().split())) for _ in range(K)]

for s, t in ST:
    if s < t:
        day, now = 0, s

        for l, r in LR:
            day += 1

            if now >= l: now = max(now, r)
            if now >= t: break

    else:
        day, now = 0, s

        for l, r in LR:
            day += 1

            if now <= r: now = min(now, l)
            if now <= t: break

    print(day)
