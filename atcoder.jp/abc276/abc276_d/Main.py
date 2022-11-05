def main():
    N = int(input())
    A = list(map(int, input().split()))

    arr = [[0]*N for _ in range(2)]
    st = set()
    for i, ai in enumerate(A):
        while not ai % 2:
            ai //= 2
            arr[0][i] += 1
        while not ai % 3:
            ai //= 3
            arr[1][i] += 1
        st.add(ai)

    if len(st) > 1: ans = -1
    else:
        arr[0].sort(), arr[1].sort()
        ans = sum(arr[0]) - arr[0][0]*N + sum(arr[1]) - arr[1][0]*N

    print(ans)


if __name__ == '__main__': main()
