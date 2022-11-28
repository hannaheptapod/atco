def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    arr_s, arr_t = [[[x[i][j] for i in range(H)] for j in range(W)] for x in (S, T)]
    arr_s.sort()
    arr_t.sort()

    ans = 'Yes' if arr_s == arr_t else 'No'
    print(ans)


if __name__ == '__main__': main()
