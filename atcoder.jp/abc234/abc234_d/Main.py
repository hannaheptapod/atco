import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

h = P[:K]
heapq.heapify(h)
m = heapq.heappop(h)
print(m)
heapq.heappush(h, m)

for i in range(K, N):
    heapq.heappush(h, P[i])
    heapq.heappop(h)
    m = heapq.heappop(h)
    print(m)
    heapq.heappush(h, m)
