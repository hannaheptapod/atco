S = input()
T = input()

res = ('You will lose', 'You can win')

ans = 1
for i in range(len(S)):
    if S[i] == '@':
        if T[i] in 'atcoder@': continue
        ans = 0
        break
    elif T[i] == '@':
        if S[i] in 'atcoder': continue
        ans = 0
        break
    elif S[i] == T[i]: continue
    ans = 0
    break

print(res[ans])
