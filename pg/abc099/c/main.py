N = int(input())

ans = N

def dec2n(x, n):
    y = 0
    while x:
        y += x%n
        x //= n
    return y

for i in range(0, N + 1, 9):
    tmp = dec2n(i, 9)
    tmp += dec2n(N-i, 6)

    ans = min(ans, tmp)

print(ans)