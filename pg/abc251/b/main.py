from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

st = set(A)
st |= {sum(c) for c in combinations(A, 2)}
st |= {sum(c) for c in combinations(A, 3)}
ans = sum([n in st for n in range(1, W+1)])
print(ans)
