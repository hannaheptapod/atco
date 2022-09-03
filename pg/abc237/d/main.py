from collections import deque

N = int(input())
S = input()

deq = deque([N])
for i in range(N-1, -1, -1):
    if S[i] == 'L': deq.append(i)
    else: deq.appendleft(i)

print(*deq)
