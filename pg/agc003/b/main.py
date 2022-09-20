def main():
    N = int(input())
    A = [0] + [int(input()) for _ in range(N)]

    ans = 0
    for i in range(N):
        ans += A[i]//2
        A[i] %= 2
        if A[i] and A[i+1]:
            ans += 1
            A[i] = 0
            A[i+1] -= 1
    ans += A[-1]//2

    print(ans)


if __name__ == '__main__': main()
