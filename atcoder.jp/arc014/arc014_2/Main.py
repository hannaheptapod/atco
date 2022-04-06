N = int(input())

s = set()
for i in range(N):
    W = input()

    if W in s:
        ans = 'WIN' if i%2 else 'LOSE'
        break

    try:
        if W[0] != tail:
            ans = 'WIN' if i%2 else 'LOSE'
            break
    except Exception: pass

    s.add(W)
    tail = W[-1]

else: ans = 'DRAW'

print(ans)
