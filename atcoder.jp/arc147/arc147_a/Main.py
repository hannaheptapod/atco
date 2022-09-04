import heapq

N = int(input())
A = list(map(int, input().split()))

arr = [-ai for ai in A]
heapq.heapify(arr)

ans = 0
mn = min(A)
while len(arr) > 1:
    ans += 1
    ai = -heapq.heappop(arr)%(mn)
    if ai:
        heapq.heappush(arr, -ai)
        mn = min(mn, ai)

print(ans)
