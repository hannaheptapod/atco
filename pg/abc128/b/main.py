n = int(input())
l = []
for i in range(1, n+1):
    s, p = input().split()
    p = -int(p)
    l.append([s, p, i])
l.sort()
_ = [print(li[2]) for li in l]