def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    ans = [0]*W
    for ci in C:
        for j in range(W): ans[j] += int(ci[j] == '#')

    print(*ans)


if __name__ == '__main__': main()
