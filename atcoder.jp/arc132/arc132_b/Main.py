def main():
    N = int(input())
    P = list(map(int, input().split()))

    diff = P[1]-P[0]
    if diff == 1 or diff == 1-N: ans = min((N+1-P[0])%N, P[-1]%N+2)
    else: ans = min(P[0]%N+1, (N+1-P[-1])%N+1)

    print(ans)


if __name__ == '__main__': main()
