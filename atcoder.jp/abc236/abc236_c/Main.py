N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

st = set(T)
for si in S: print('Yes' if si in st else 'No')
