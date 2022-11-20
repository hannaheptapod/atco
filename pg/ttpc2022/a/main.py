def main():
    X, Y = map(int, input().split())

    ans = common_divisor(X-2015, Y-2015)
    print(*ans, sep='\n')


def common_divisor(a, b):
    from math import gcd

    st = set()
    g = gcd(a, b)

    for i in range(1, int(g**0.5)+1):
        if g % i == 0:
            st.add(i)
            st.add(g//i)

    arr = list(st)
    arr.sort()
    return arr


if __name__ == '__main__': main()
