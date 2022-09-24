def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(A)

    tot, b = 0, 0
    for i in range(N):
        prev = b
        b = min(B[i], prev + -(-(K-tot)//(N-i)))
        tot += (b-prev)*(N-i)
        if tot >= K:
            rem = N-i - (tot-K)
            break

    cnt = 0
    ans = [0]*N
    for i in range(N):
        if A[i] < b: continue
        ans[i] = A[i] - b + 1 - int(cnt < rem)
        cnt += 1

    print(*ans)


if __name__ == '__main__': main()
