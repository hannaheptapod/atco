def fact(n):
    cnt = 0
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            cnt += 1
            n //= i
    if n != 1:
        cnt += 1
    return cnt

n = int(input())
ans = 0

f = fact(n)
for i in range(n):
    if 1<<i >= f: ans = i; break
print(ans)