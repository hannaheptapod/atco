def main():
    N = int(input())
    A = list(map(int, input().split()))

    def solve():
        A.sort(reverse=True)
        sm = sum(A)
        ave, mod = divmod(sm, N)

        ans = sum([abs(ai - (ave + int(i < mod))) for i, ai in enumerate(A)])//2
        return ans

    ans = solve()
    print(ans)

    return

if __name__ == '__main__': main()
