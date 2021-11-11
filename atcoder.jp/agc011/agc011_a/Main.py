n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()
num = load = time = 0
for ti in t:
    if load == 0:
        num += 1
        time = ti+k
        load += 1
    elif ti <= time and load < c: load += 1
    else:
        num += 1
        load = 1
        time = ti+k
print(num)