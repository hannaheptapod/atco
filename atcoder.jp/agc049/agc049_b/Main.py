def main():
    N = int(input())
    arr_s, ARR_T = (list(map(int, input())) for _ in range(2))

    ans = 0
    l = 1
    for i in range(N):
        if arr_s[i] == ARR_T[i]: continue

        for j in range(max(i+1, l), N):
            if not arr_s[j]: continue

            arr_s[i], arr_s[j] = 1-arr_s[i], 1-arr_s[j]
            ans += j-i
            l = j+1
            break

        if arr_s[i] != ARR_T[i]: ans = -1; break

    print(ans)


if __name__ == '__main__': main()
