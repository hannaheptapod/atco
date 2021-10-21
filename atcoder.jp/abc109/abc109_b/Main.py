n = int(input())
w = [input() for _ in range(n)]
s = set(w)
if len(s) < n: ans = 'No'
else:
    for i in range(n - 1):
        if w[i][-1] != w[i + 1][0]:
            ans = 'No'
            break
        else: continue
    else: ans = 'Yes'
print(ans)