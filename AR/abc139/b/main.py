a, b = map(int, input().split())
sm = 1
for i in range(20):
    if sm >= b:
        print(i)
        break
    else:
        sm += a-1