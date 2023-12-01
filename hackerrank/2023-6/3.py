# Sherlock and Squares

from bisect import bisect_left, bisect_right


def main():
    q = int(input())

    global arr_squares
    arr_squares = [i**2 for i in range(1, 10 ** 5)]

    for _ in range(q):
        a, b = map(int, input().split())
        ans = squares(a, b)
        print(ans)


def squares(a, b):
    return bisect_right(arr_squares, b) - bisect_left(arr_squares, a)


if __name__ == '__main__': main()
