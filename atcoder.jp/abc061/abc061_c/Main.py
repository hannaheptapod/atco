from collections import deque
from bisect import insort
n, k = map(int, input().split())
dic, lis = {}, []
for _ in range(n):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = 0
        insort(lis, a)
    dic[a] += b
deq = deque(lis)
cnt = 0
while deq and cnt < k:
    ans = deq.popleft()
    cnt += dic[ans]
print(ans)