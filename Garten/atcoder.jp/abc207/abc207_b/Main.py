a, b, c, d = map(int, input().split())
diff = c * d - b
ans = -1
if diff > 0:
    ans = (a + diff - 1)//(diff)
print(ans)