import heapq
n, m = map(int, input().split())
a = list(map(lambda x: -int(x), input().split()))
heapq.heapify(a)
for _ in range(m):
    mx = heapq.heappop(a)
    mx = -(-mx // 2)
    heapq.heappush(a, mx)
ans = -sum(a)
print(ans)