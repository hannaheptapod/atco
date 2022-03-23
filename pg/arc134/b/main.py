from collections import Counter
import array

N = int(input())
arr = array.array('i', list(map(ord, list(input()))))
cnt = Counter(arr)

tail = N
for head in range(N):
    h = arr[head]
    cnt[h] -= 1

    for i in range(h):
        if cnt[i]:
            target = i
            break
    else: continue

    while head < tail:
        tail -= 1
        t = arr[tail]
        cnt[t] -= 1

        if t == target:
            arr[head], arr[tail] = t, h
            break

    if tail < head: break

ans = ''.join([chr(ai) for ai in arr])
print(ans)
