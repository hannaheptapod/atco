def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: sum(x), reverse=True)
    ans = sum((-1)**(i%2) * arr[i][i%2] for i in range(N))
    print(ans)


if __name__ == '__main__': main()
