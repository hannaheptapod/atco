def main():
    N, Q = map(int, input().split())
    arr = [[0]] + [list(map(int, input().split())) for _ in range(N)]

    for _ in range(Q):
        s, t = map(int, input().split())
        print(arr[s][t])


if __name__ == '__main__': main()
