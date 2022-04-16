from bisect import bisect_left as bil, bisect_right as bir
import array

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

id = [array.array('i', []) for _ in range(N+1)]
for i in range(N): id[A[i]].append(i+1)

for _ in range(Q):
    l, r, x = map(int, input().split())

    ans = bir(id[x], r) - bil(id[x], l)
    print(ans)
