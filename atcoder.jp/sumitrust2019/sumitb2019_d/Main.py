n = int(input())
s = input()
ans = 0
for i in range(1000):
    pin = f'{i:03}'
    d = 0
    for sj in s:
        if pin[d] == sj:
            d += 1
            if d == 3:
                ans += 1
                break
print(ans)