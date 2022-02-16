from bisect import bisect_left as bl, bisect_right as br

n = int(input())
a, b, c = [sorted(list(map(int, input().split()))) for _ in range(3)]

ans = sum([bl(a, bi)*(n - br(c, bi)) for bi in b])

print(ans)