n, k = map(int, input().split())
td = []
for _ in range(n):
    td.append(list(map(int, input().split())))
td.sort(reverse=True, key=lambda x: (x[1], x[0]))

