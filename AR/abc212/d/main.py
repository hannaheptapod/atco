import heapq
Q = int(input())
q = []
n1 = []
heapq.heapify(n1)
n2 = 0
for i in range(Q):
    q.append(list(map(int, input().split())))
for qi in q:
    if qi[0] == 1:
        heapq.heappush(n1, qi[1] - n2)
    elif qi[0] == 2:
        n2 += qi[1]
    else:
        print(heapq.heappop(n1) + n2)
        