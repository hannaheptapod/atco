def main():
    N = int(input())
    S = list(map(int, input().split()))

    ans = [0]*N
    ans[0], sm = S[0], S[0]
    for i in range(1, N):
        ans[i] = S[i] - sm
        sm += ans[i]

    print(*ans)


if __name__ == '__main__': main()
