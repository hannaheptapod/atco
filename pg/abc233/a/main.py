def main():
    X, Y = map(int, input().split())

    ans = max(0, -(-(Y-X) // 10))
    print(ans)


if __name__ == '__main__': main()
