def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = solve(N, A)
    print(ans)


def solve(N, A):
    flip = 0
    f, e = 0, N-1

    for _ in range(N):
        if flip == A[e]:
            e -= 1
            continue
        if flip == A[f]:
            f += 1
            flip = 1-flip
            continue
        else: return 'No'
    else: return 'Yes'


if __name__ == '__main__': main()
