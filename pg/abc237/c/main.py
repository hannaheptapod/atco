S = input()

N = len(S)
cnt = 0
for si in S:
    if si == 'a': cnt -= 1
    else: break
for sj in S[::-1]:
    if sj == 'a': cnt += 1
    else: break

ans = 'Yes' if cnt >= 0 and S[:N-cnt] == S[N-cnt-1::-1] else 'No'
print(ans)
