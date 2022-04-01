N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cnt = [0]*(10**5 + 1)
for ai in A: cnt[ai] += 1

sm = sum(A)
for _ in range(Q):
    b, c = map(int, input().split())
    cb = cnt[b]
    sm += cb*(c - b)
    print(sm)

    cnt[b], cnt[c] = 0, cnt[c] + cb
