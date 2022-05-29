Q = int(input())
s = {}
mx, mn = 0, 10**9
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        if query[1] not in s:
            s[query[1]] = 1
            mx = max(mx, query[1])
            mn = min(mn, query[1])
        else: s[query[1]] += 1

    elif query[0] == 2:
        if query[1] not in s: continue
        s[query[1]] -= min(query[2], s[query[1]])
        if not s[query[1]]:
            s.pop(query[1])
            if not s:
                mx, mn = 0, 10**9
                continue
            if mx == query[1]: mx = max(s)
            if mn == query[1]: mn = min(s)

    else: ans.append(mx-mn)

print(*ans, sep='\n')
