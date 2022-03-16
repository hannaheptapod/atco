n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = c*n
for ev in range(1, 10+1):
    tmp_ev = sum([int(a_ev != ev) for a_ev in a[::2]])
    for od in range(1, 10+1):
        if ev == od: continue

        tmp_od = sum(int(a_od != od) for a_od in a[1::2])
        ans = min(ans, c*(tmp_ev + tmp_od))

print(ans)
