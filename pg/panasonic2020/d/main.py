from bisect import insort

N = int(input())
ans = []


def make(s, k):
    if len(s) == N:
        insort(ans, s)
        return
    for i in range(k+1):
        make(s+chr(ord('a')+i), max(k, i+1))


make('a', 1)
print(*ans, sep='\n')
