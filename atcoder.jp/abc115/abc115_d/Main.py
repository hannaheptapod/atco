n, x = map(int, input().split())

pat, tot = [1], [1]
for i in range(1, n+1):
    pat += [2*pat[i-1] + 1]
    tot += [2*tot[i-1] + 3]

def cnt(lv, h):
    if lv == 0: return 1
    elif h < 1: return 0
    else: h -= 1

    if h < tot[lv-1]: return cnt(lv-1, h)
    else: h -= tot[lv-1]

    if h < 1: return pat[lv-1] + 1
    else: h -= 1

    if h < tot[lv-1]: return pat[lv-1] + 1 + cnt(lv-1, h)
    else: h -= tot[lv-1]

    return 2*pat[lv-1] + 1

ans = cnt(n, x-1)

print(ans)