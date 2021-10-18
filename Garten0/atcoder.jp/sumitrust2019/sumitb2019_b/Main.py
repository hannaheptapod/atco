n = int(input())
ans = ':('
for i in range(50001):
    if (i * 1.08) // 1 == n:
        ans = i
        break
print(ans)