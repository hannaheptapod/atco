import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self):
        self.parent = -1
        self.children = []

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

tree = [Node() for _ in range(N)]

