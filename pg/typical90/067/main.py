nk = list(input().split())
n, k = int(nk[0], 8), int(nk[1])

def octnovoct(n):
    s_nov = str()
    for _ in range(20):
        tmp = n % 9
        if tmp == 8:
            tmp = 5
        s_nov = str(tmp) + s_nov
        if n < 9:
            break
        else:
            n = n // 9
    n_nov = int(s_nov, 8)
    return n_nov

for i in range(k):
    n = octnovoct(n)

print(oct(n)[2:])