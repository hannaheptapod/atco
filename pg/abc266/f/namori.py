import sys
from collections import deque

sys.setrecursionlimit(10**9)


class Namori:
    def __init__(self, node_size):
        self.V = node_size
        self.G = [[] for _ in range(self.V)]
        self.deg = [0 for _ in range(self.V)]
        self.loop = []
        self.root = [-1 for _ in range(self.V)]
        self.flag = [False for _ in range(self.V)]

    def add_edge(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)
        self.deg[u] += 1
        self.deg[v] += 1

    def dfs(self, u):
        self.loop.append(u)
        for v in self.G[u]:
            if self.flag[v]: continue
            self.flag[v] = True
            self.dfs(v)

    def build(self):
        self.graph = [[] for _ in range(self.V)]
        self.que = deque()

        for i in range(self.V):
            if self.deg[i] == 1:
                self.que.append(i)
                self.flag[i] = True

        while self.que:
            p = self.que.popleft()
            for v in self.G[p]:
                if self.flag[v]: continue
                self.deg[v] -= 1
                self.graph[v].append(p)
                self.graph[p].append(v)
                if self.deg[v] > 1: continue
                self.que.append(v)
                self.flag[v] = True

        for i in range(self.V):
            if self.flag[i]: continue
            self.flag[i] = True
            self.dfs(i)
            break

        for r in self.loop:
            deq = deque([r])
            while deq:
                p = deq.popleft()
                if self.root[p] >= 0: continue
                self.root[p] = r
                for v in self.graph[p]:
                    if self.root[v] >= 0: continue
                    deq.append(v)
