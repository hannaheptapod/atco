from itertools import accumulate


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    acc = list(accumulate(A))

    print(acc)


if __name__ == '__main__': main()
