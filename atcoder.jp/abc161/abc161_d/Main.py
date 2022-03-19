from collections import deque

K = int(input())

deq = deque([i for i in range(1, 10)])
for _ in range(K):
    x = deq.popleft()
    if x%10: deq.append(10*x + x%10 - 1)
    deq.append(10*x + x%10)
    if x%10 < 9: deq.append(10*x + x%10 + 1)

ans = x
print(x)
