a, b = map(int, input().split())
for i in range(256):
    if a ^ i == b:
        ans = i
        break
print(ans)