def main():
    N, M = map(int, input().split())

    st = [set() for _ in range(N+1)]
    for _ in range(M):
        arr = list(map(int, input().split()))

        for i in range(1, arr[0]):
            for j in range(i+1, arr[0]+1):
                st[arr[i]].add(arr[j])
                st[arr[j]].add(arr[i])

    ans = 'Yes' if all(len(s) == N-1 for s in st[1:]) else 'No'
    print(ans)


if __name__ == '__main__': main()
