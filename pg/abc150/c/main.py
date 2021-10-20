from itertools import permutations
n = int(input())
per = list(permutations([i for i in range(1, n+1)]))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
ans = abs(per.index(tuple(p)) - per.index(tuple(q)))
print(ans)