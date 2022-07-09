from bisect import insort
import array

N = int(input())
dic = {i: [] for i in range(N)}
ps = {}
dp = []
for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        dic[i].append([p, e])

        if p not in ps:
            ps[p] = [0]
            insort(dp, p)
        insort(ps[p], e)

st = set()
M = len(ps)
for i in range(N):
    arr = array.array('i', [])

    for p, e in dic[i]:
        if ps[p][-2] < e: insort(arr, p)

    st.add(''.join(str(ai) for ai in arr))

ans = len(st)
print(ans)
