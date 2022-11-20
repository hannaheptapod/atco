def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    arr = A
    for _ in range(K): arr = arr[1:] + [0]

    print(*arr)


if __name__ == '__main__': main()
