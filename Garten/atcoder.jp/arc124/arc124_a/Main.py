N, K = map(int, input().split())
c, k = [], []
for i in range(K):
    ci, ki = input().split()
    c.append(ci)
    k.append(int(ki))

ans = 1
for i in range(N):
    a = K
    p = i + 1

    for j in range(K):
        if k[j] is p:
            a = 1
            break
        elif (c[j] == 'L' and p < k[j]) or (c[j] == 'R' and p > k[j]):
            a -= 1

    ans *= a

print(ans % 998244353)
