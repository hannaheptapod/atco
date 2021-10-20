n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = [0] * n
sn = s[n - 1] + t[n - 1]
for i in range(2 * n):
    i = i % n
    tk = t[i]
    if sn <= tk:
        ans[i] = sn
    else:
        ans[i] = tk
        sn = tk
    sn += s[i]
_ = [print(ai) for ai in ans]