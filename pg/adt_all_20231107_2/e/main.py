def main():
    S, K = input().split()
    K = int(K)

    ans = solve(S, K)
    print(ans)


def solve(S, K):
    from itertools import permutations

    perms = sorted(set(permutations(S)))
    return ''.join(perms[K-1])


if __name__ == '__main__': main()
