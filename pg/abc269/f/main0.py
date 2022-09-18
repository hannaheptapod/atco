MOD = 998244353
INV = pow(2, -1, MOD)


def main():
    global N, M
    N, M = map(int, input().split())
    Q = int(input())

    for _ in range(Q):
        a, b, c, d = map(int, input().split())

        ans = area(a, b, c, d) if (a-c)%2 == (b-d)%2 else area(a, b, c, d+1)-area(a, b, d+1, d+1)
        print(ans%MOD)


def calc(i, j): return (i-1)*M+j


def area(a, b, c, d):
    if abs(a-b): mn, mx = calc(a+(a+c)%2, c), calc(b-(b+d)%2, d)
    elif abs(c-d): mn, mx = calc(a, c+(a+c)%2), calc(b, d-(b+d)%2)
    else: mn, mx = [calc(a, c) if not (a+c)%2 else 0]*2

    if (a-b)%2 or (c-d)%2: return (mn+mx)*INV*(((b-a+1)*(d-c+1))//2) % MOD
    return (mn+mx)*INV*(((b-a+1)*(d-c+1)+(1-(a+c)%2))//2) % MOD


if __name__ == '__main__': main()
