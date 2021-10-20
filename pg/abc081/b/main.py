N = int(input())
A = list(map(int, input().split()))
ctr = [0]*N
for i in range(N):
    a = A[i]
    flag = 0
    while flag == 0:
        if a%2 == 0:
            a /= 2
            ctr[i] += 1
        else:
            flag = 1
ans = min(ctr)
print(ans)