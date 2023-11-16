from itertools import permutations


def main():
    N, M = map(int, input().split())
    Tak, Aok = [[] for _ in range(N)], [[] for _ in range(N)]
    for _ in range(M):
        i, j = map(int, input().split())
        Tak[i-1].append(j-1)
        Tak[j-1].append(i-1)
    for _ in range(M):
        i, j = map(int, input().split())
        Aok[i-1].append(j-1)
        Aok[j-1].append(i-1)

    print('Yes' if are_isomorphic(Tak, Aok) else 'No')


def are_isomorphic(Tak, Aok):
    N = len(Tak)

    # Generate all permutations of Aok's vertices
    for perm in permutations(range(N)):
        # Create a new graph by reordering Aok's vertices
        Aok_perm = [[perm.index(j) for j in Aok[i]] for i in perm]

        # Check if Tak and the reordered Aok are the same
        if all(sorted(Tak[i]) == sorted(Aok_perm[i]) for i in range(N)):
            return True

    # If no permutation makes Tak and Aok the same, they are not isomorphic
    return False


if __name__ == '__main__': main()
