from itertools import chain


def main():
    H, M = map(int, input().split())

    fr = H*60 + M
    for time in chain(range(fr, 24*60), range(fr)):
        h0, m0 = divmod(time, 60)
        h1, m1 = 10*(h0//10)+m0//10, 10*(h0%10)+m0%10

        if 0 <= h1 < 24 and 0 <= m1 < 60: break

    print(f'{h0:02} {m0:02}')


if __name__ == '__main__': main()
