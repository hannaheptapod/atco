n = int(input())
t, a = map(int, input().split())
ha = (t - a) / 0.006
h = list(map(int, input().split()))
dis = [abs(hi - ha) for hi in h]
ans = dis.index(min(dis)) + 1
print(ans)