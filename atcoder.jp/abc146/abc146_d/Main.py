import sys
sys.setrecursionlimit(10**6)


def main():
    global N, E
    N = int(input())
    E = [{} for _ in range(N)]
    for i in range(N-1):
        a, b = map(lambda x: int(x)-1, input().split())
        E[a][b] = E[b][a] = i
    K = max(len(E[i]) for i in range(N))

    global ans
    ans = [0]*(N-1)

    dfs(0)

    print(K)
    print(*ans, sep='\n')


def dfs(cu, pa=-1, col=0):
    used = set()
    used.add(col)
    c = 1
    for to in E[cu].keys():
        if to == pa: continue
        while c in used: c += 1
        ans[E[cu][to]] = c
        dfs(to, cu, c)
        c += 1


if __name__ == '__main__': main()
