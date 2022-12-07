from math import log, log2


def main():
    P = float(input())

    x = -1.5 * log2(3 / (2*P*log(2)))

    ans = x + P/pow(2, x/1.5) if x>0 else P
    print(ans)


if __name__ == '__main__': main()
