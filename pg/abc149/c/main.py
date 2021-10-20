x = int(input())
prime = [2]
if x == 2: ans = 2
elif x > 2:
    for i in range(3, int(x**0.5) + 1):
        if all([i % p for p in prime]): prime += [i]
    while True:
        if all([x % p for p in prime]):
            ans = x
            break
        else:
            x += 1
print(ans)