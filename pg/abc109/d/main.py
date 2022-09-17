def main():
    H, W = map(int, input().split())
    a = [list(map(lambda x: int(x)%2, input().split())) for _ in range(H)]

    ans = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j]:
                ans += [(i+1, j+1, i+1, j+2)]
                a[i][j+1] = 1-a[i][j+1]
        if i == H-1: break
        if a[i][-1]:
            ans += [(i+1, W, i+2, W)]
            a[i+1][-1] = 1-a[i+1][-1]

    print(len(ans))
    _ = [print(*ai) for ai in ans]


if __name__ == '__main__': main()
