from collections import deque


def main():
    global N, E
    N = int(input())
    E = [{} for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        E[u-1][v-1] = E[v-1][u-1] = w%2

    ans = dfs()
    print(*ans, sep='\n')


def dfs():
    colors = [-1]*N

    deq= deque([(0, 0)])
    while deq:
        v, c = deq.pop()
        if colors[v] != -1: continue
        colors[v] = c

        for u in E[v]: deq.append((u, c^E[v][u]))

    return colors


if __name__ == '__main__': main()
