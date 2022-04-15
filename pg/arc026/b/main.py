from collections import Counter


def main():
    N = int(input())

    ans = calc(N)
    print(ans)


def prime_factorize(num):
    a = []

    while num % 2 == 0:
        a.append(2)
        num //= 2

    f = 3

    while f * f <= num:
        if num % f == 0:
            a.append(f)
            num //= f
        else: f += 2

    if num != 1: a.append(num)

    return Counter(a)


def calc(num):
    cnt = prime_factorize(num)

    tot = 1
    for p, e in cnt.items(): tot *= (p**(e+1) - 1) // (p - 1)

    if tot == 2*num: return 'Perfect'
    if tot < 2*num: return 'Deficient'
    return 'Abundant'


if __name__ == '__main__': main()
