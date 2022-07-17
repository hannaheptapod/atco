N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = [[A[i], B[i], A[i]+B[i], -(i+1)] for i in range(N)]

st = set()


def f(id, n):
    arr.sort(key=lambda x: (x[id], x[-1]), reverse=True)
    cnt = 0
    for i in range(N):
        if cnt == n: break
        if -arr[i][-1] not in st:
            st.add(-arr[i][-1])
            cnt += 1


f(0, X)
f(1, Y)
f(2, Z)

ans = sorted(st)
print(*ans, sep='\n')
