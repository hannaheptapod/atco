import bisect

N = int(input())
w = [int(input()) for _ in range(N)]

mt = [w[0]]
for wi in w[1:]:
    if wi > mt[-1]: mt.append(wi)
    else:
        id = bisect.bisect_left(mt, wi)
        mt[id] = wi

ans = len(mt)
print(ans)
