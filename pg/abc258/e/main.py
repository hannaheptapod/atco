from bisect import bisect_left as bil

N, Q, X = map(int, input().split())
W = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

sm = [0]*(2*N)
for i in range(2*N-1): sm[i+1] = sm[i]+W[i%N]

last = 0
cnt, arr = [], [0]
st = set(arr)

d = X//sm[N] * N
X %= sm[N]

for i in range(N):
    nxt = bil(sm, X+sm[last])

    cnt.append(d+nxt-last)
    if nxt%N in st:
        loop = arr.index(nxt%N)
        break
    arr.append(nxt%N)
    st.add(nxt%N)
    last = nxt%N

for ki in K: print(cnt[ki-1] if ki-1 < loop else cnt[loop+(ki-1-loop)%(len(cnt)-loop)])
