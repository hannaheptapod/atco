def main():
    _ = int(input())
    A = list(map(int, input().split()))

    ans = calc(A)
    print(ans)


def calc(arr):
    ret, sm, b = 0, sum(arr), 1

    for a in arr:
        if b < a: return -1
        ret += b
        sm -= a
        b = min(2 * (b-a), sm)

    return ret


if __name__ == '__main__': main()
