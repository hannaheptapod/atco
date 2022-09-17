MOD = 998244353
INV = pow(2, -1, MOD)


def main():
    global N, M
    N, M = map(int, input().split())
    Q = int(input())

    for _ in range(Q):
        a, b, c, d = map(int, input().split())

        ans = area(a, b, c, d)
        print(ans)


def area(a, b, c, d):
    if a > b or c > d: return 0
    if (b-a)%2 != (d-c)%2:
        if (d-c)%2: return (area(a, b, c, d-1) + area(a, b, d, d)) % MOD
        return (area(a, b-1, c, d) + area(b, b, c, d)) % MOD

    ave = ((a+b)%MOD*INV-1)*M + (c+d)%MOD*INV
    cnt = (b-a+1)* (d-c+1)//2 + int((b-a)%2==0 and (a+c)%2==0)
    ave, cnt = ave % MOD, cnt % MOD
    return ave*cnt % MOD


if __name__ == '__main__': main()
