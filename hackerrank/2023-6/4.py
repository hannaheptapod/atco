def main():
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    for i in range(n//2): arr[i][1] = '-'

    arr.sort(key=lambda x: int(x[0]))
    print(' '.join([x[1] for x in arr]))


if __name__ == '__main__': main()
