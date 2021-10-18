n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split())) + [l]
d = [a[i+1] - a[i] for i in range(n + 1)]

def howmany(dmin):
    num = 0
    tmp = 0
    for di in d:
        tmp += di
        if tmp >= dmin:
            num += 1
            tmp = 0
    return num >= k + 1

def bisec():
    ok = -1
    ng = l + 1

    while ok + 1 < ng:
        md = (ok + ng) // 2
        if howmany(md): ok = md
        else: ng = md
    return ok

ans = bisec()
print(ans)