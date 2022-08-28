from itertools import permutations

N = int(input())
A = sorted(input().split(), key=lambda x: int(x), reverse=True)

ans = max(int(''.join(p)) for p in permutations(A[:3]))
print(ans)
