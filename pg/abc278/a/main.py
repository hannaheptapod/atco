def main():
    _, K = map(int, input().split())
    A = list(map(int, input().split()))

    arr = A + [0]*K

    ans = arr[K:]
    print(*ans)


if __name__ == '__main__': main()
