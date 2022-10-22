def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))

    ans = [0]*2 + [-1]*2*N
    for i in range(1, N+1): ans[2*i] = ans[2*i + 1] = ans[A[i]] + 1

    print(*ans[1:], sep='\n')


if __name__ == '__main__': main()
