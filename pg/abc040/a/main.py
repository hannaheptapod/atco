def main():
    n, x = map(int, input().split())

    ans = min(x-1, n-x)
    print(ans)


if __name__ == '__main__': main()
