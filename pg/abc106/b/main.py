def count_div(n):
    ctr = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ctr += 1
            if i != n // i:
                ctr += 1

    return ctr
    
N = int(input())

ans = 0
for i in range(1, N + 1, 2):
    if count_div(i) == 8:
        ans += 1

print(ans)