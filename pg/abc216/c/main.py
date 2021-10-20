n = int(input())
ans = str()

for i in range(120):
    if n % 2:
        ans = 'A' + ans
        n -= 1
    else:
        ans = 'B' + ans
        n //= 2
    if n == 0:
        print(ans)
        break
    else:
        continue
