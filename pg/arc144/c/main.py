N, K = map(int, input().split())


def f(x, y):
    if x <= 3*K: return list(i+K for i in range(y+1, y+x-K+1))+list(i-x+K for i in range(y+x-K+1, y+x+1))
    elif x <= 4*K:
        return list(i+K for i in range(y+1, y+K+1)) +\
            list(i-K for i in range(y+K+1, y+x-2*K+1)) +\
            list(i+K for i in range(y+x-2*K+1, y+x-K+1)) +\
            list(i-2*K for i in range(y+x-K+1, y+3*K+1)) +\
            list(i-K for i in range(y+3*K+1, y+x+1))
    else: return list(i+K for i in range(y+1, y+K+1))+list(i for i in range(y+1, y+K+1)) + f(x-2*K, y+2*K)


ans = f(N, 0) if N >= 2*K else [-1]
print(*ans)
