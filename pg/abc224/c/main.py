n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 2):
    pi = p[i]
    for j in range(i + 1, n - 1):
        pj = p[j]
        ij = [pj[0] - pi[0], pj[1] - pi[1]]
        for k in range(j + 1, n):
            pk = p[k]
            ik = [pk[0] - pi[0], pk[1] - pi[1]]
            if ij[0]*ik[1] != ij[1]*ik[0]: ans += 1
print(ans)