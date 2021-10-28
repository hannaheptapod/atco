n = int(input())
a = list(map(int, input().split()))
sm = 0
mcnt = 0
mn = 10**10
for ai in a:
    sm += abs(ai)
    if ai < 0: mcnt += 1
    mn = min(mn, abs(ai))
if mcnt % 2: sm -= 2 * mn
print(sm)