S, T = input(), input()
l, r = 0, len(T)

ls, lt = len(S), len(T)
for i, si in enumerate(S):
    if i < lt and '?' not in (si, T[i]) and si != T[i]: r = min(r, i)
    if i >= ls-lt and '?' not in (si, T[i-ls+lt]) and si != T[i-ls+lt]: l = max(l, i-ls+lt+1)

ans = ['Yes' if l <= i <= r else 'No' for i in range(len(T)+1)]
print(*ans, sep='\n')
