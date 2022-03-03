from collections import Counter

N = int(input())
S = input()

cnt = Counter(S)
ans = cnt['R']*cnt['G']*cnt['B']

for i in range(N-2):
    for d in range(1, (N - i + 1)//2):
        if len(set((S[i], S[i + d], S[i + 2*d]))) == 3: ans -= 1

print(ans)
