from heapq import heappush, heappop


class Dijkstra:
    class Edge:
        def __init__(self, end, cost):
            self.to = end
            self.cost = cost

    def __init__(self, node_size, inf):
        self._node = node_size
        self._graph = [[] for _ in range(self._node)]
        self.inf = inf
        self.dist = [self.inf for _ in range(self._node)]

    def add_edge(self, st, ed, cost):
        self._graph[st].append(self.Edge(ed, cost))
        self._graph[ed].append(self.Edge(st, cost))

    def solve(self, start):
        que = []
        self.dist[start] = 0
        heappush(que, (0, start))
        while que:
            cur_cost, cur_vertex = heappop(que)
            if self.dist[cur_vertex] < cur_cost:
                continue
            for e in self._graph[cur_vertex]:
                if self.dist[e.to] > cur_cost + e.cost:
                    self.dist[e.to] = cur_cost + e.cost
                    heappush(que, (self.dist[e.to], e.to))
