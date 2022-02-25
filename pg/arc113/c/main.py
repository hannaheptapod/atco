S = input()

ans = 0
lg, prev, now, cnt = len(S), '#', S[0], 0
for i in range(lg):
    if S[i] == now: cnt += 1
    elif cnt >= 2:
        if now == prev: ans -= cnt-1
        else: ans += lg - i
        prev, now, cnt = now, S[i], 1
    else:
        if S[i] == prev: ans -= 1
        now, cnt = S[i], 1
if cnt >= 2 and now == prev: ans -= cnt-1

print(ans)