from collections import deque

N = int(input())
A = [[0]*(i+1)+list(map(int, input().split())) for i in range(2*N-1)]

deq = deque()
used = [False]*(2*N)


def solve():
    if len(deq) == N:
        ret = 0
        for i, j in deq: ret ^= A[i][j]
        return ret

    for i in range(2*N-1):
        if not used[i]: break
    used[i] = True

    ret = 0
    for j in range(i+1, 2*N):
        if not used[j]:
            deq.append((i, j))
            used[j] = True
            ret = max(ret, solve())
            deq.pop()
            used[j] = False

    used[i] = False
    return ret


ans = solve()
print(ans)
