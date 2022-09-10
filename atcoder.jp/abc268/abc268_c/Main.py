from collections import defaultdict

N = int(input())
p = list(map(int, input().split()))

dic = defaultdict(int)
for i in range(N):
    dic[(p[i]-(i-1))%N] += 1
    dic[(p[i]-i)%N] += 1
    dic[(p[i]-(i+1))%N] += 1

ans = max(dic.values())
print(ans)
