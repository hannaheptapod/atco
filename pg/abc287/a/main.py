from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

cnt = Counter(S)

ans = 'Yes' if cnt['For'] > N//2 else 'No'
print(ans)
