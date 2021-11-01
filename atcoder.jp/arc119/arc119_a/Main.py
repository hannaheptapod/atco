n = int(input())
a, b, c = 1, 0, n-1
ans = n
while a > 0:
    b += 1
    a = n//(2**b)
    c = n%(2**b)
    ans = min(ans, a+b+c)
print(ans)