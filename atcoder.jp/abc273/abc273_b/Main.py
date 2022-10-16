from decimal import Decimal, getcontext, ROUND_HALF_UP


def main():
    X, K = map(int, input().split())

    c = getcontext()
    c.rounding = ROUND_HALF_UP

    ans = Decimal(X)
    for i in range(1, K+1): ans = round(ans, -i)

    print(int(ans))


if __name__ == '__main__': main()
