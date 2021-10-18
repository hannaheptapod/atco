def digits(num):
    dig = 0
    while num > 0:
        num //= 10
        dig += 1
    return dig
def repunit(dig):
    rep = 0
    for i in range(dig): rep += 10**i
    return rep
def count(num, dig):
    nd = digits(num)
    r = repunit(dig)
    if num < r: return 0
    else:
        cnt = 1
        for i in range(1, nd - dig + 1):
            if num < r * 10**i: break
            else: cnt += min(num - r*10**i + 1, 10**i)
        return cnt

n = int(input())
nd = digits(n)
ans = 0
for i in range(1, nd + 1): ans += count(n, i)
print(ans)