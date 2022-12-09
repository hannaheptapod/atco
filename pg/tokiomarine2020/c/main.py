def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(min(K, 50)):
        diff = [0]*N

        for i, ai in enumerate(arr):
            l, r = max(0, i-ai), min(N-1, i+ai)
            diff[l] += 1
            if r+1 < N: diff[r+1] -= 1

        for i in range(1, N): diff[i] += diff[i-1]

        arr = diff[:]

    print(*arr)


if __name__ == '__main__': main()
