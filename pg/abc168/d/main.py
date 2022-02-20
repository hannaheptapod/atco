from collections import deque

class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1
    
    def __repr__(self):
        return f'Node index:{self.index}, nears:{self.nears}, sign:{self.sign}'

N, M = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(M)]

nodes = [Node(i) for i in range(N + 1)]

for j in range(M):
    start, end = links[j]
    nodes[start].nears.append(end)
    nodes[end].nears.append(start)

queue = deque()
queue.append(nodes[1])
while queue:
    node = queue.popleft()
    print(node)

    nears = node.nears

    for near in nears:
        if nodes[near].sign == -1:
            queue.append(nodes[near])
            nodes[near].sign = node.index

if -1 in [node.sign for node in nodes][2:]: ans = 'No'
else: ans = 'Yes'

print(ans)
if ans == 'Yes':
    for k in range(2, N + 1): print(nodes[k].sign)