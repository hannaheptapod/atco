n = int(input())
lst = [0]*n
diff = 0
for i in range(n):
    ai, bi = map(int, input().split())
    lst[i] = 2*ai + bi
    diff -= ai
lst.sort(reverse=True)

ans = 0
for l in lst:
    ans += 1
    diff += l
    if diff > 0: break
print(ans)