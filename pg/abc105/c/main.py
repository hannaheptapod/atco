from collections import deque


def main():
    N = int(input())

    ans = calc(N)
    print(ans)


def calc(n):
    ret = deque()

    x, p = 0, 1
    while x != n:
        if x%abs(-2*p) != n%abs(-2*p):
            x += p
            ret.appendleft('1')
        else: ret.appendleft('0')
        p *= -2

    return ''.join(ret) if ret else '0'


if __name__ == '__main__': main()
