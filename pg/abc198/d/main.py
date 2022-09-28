def main():
    S = [list(input()) for _ in range(3)]

    ans = solve(S)
    print(*ans, sep='\n')


def solve(S):
    ret = ['UNSOLVABLE']
    st = {sij for si in S for sij in si}
    if len(st) > 10 or len(S[2]) < max(len(S[0]), len(S[1])): return ret

    comv = {k: v for k, v in zip(st, range(10))}
    N = len(S[2])
    A = [[-1]*(N - len(si)) + [comv[sij] for sij in si] for si in S]
    not_zero = [False]*10
    for si in S: not_zero[comv[si[0]]] = True

    mapped = [False]*10
    mapping = [-1]*10 + [0]

    def first(i, carry):
        if i == -1: return not carry

        if mapping[A[0][i]] != -1:
            if second(i, carry): return True
        else:
            for j in range(10):
                if mapped[j] or not j and not_zero[A[0][i]]: continue
                mapped[j] = True
                mapping[A[0][i]] = j

                if second(i, carry): return True
                mapping[A[0][i]] = -1
                mapped[j] = False

        return False

    def second(i, carry):
        if mapping[A[1][i]] != -1:
            s = mapping[A[0][i]] + mapping[A[1][i]] + carry
            x = s%10

            if mapping[A[2][i]] != -1: return mapping[A[2][i]] == x and first(i-1, s//10)
            else:
                if mapped[x] or not x and not_zero[A[2][i]]: return False
                mapping[A[2][i]] = x
                mapped[x] = True

                if first(i-1, s//10): return True
                else:
                    mapping[A[2][i]] = -1
                    mapped[x] = False
                    return False
        else:
            for j in range(10):
                if mapped[j] or not j and not_zero[A[1][i]]: continue
                mapped[j] = True
                mapping[A[1][i]] = j

                s = mapping[A[0][i]] + mapping[A[1][i]] + carry
                x = s%10

                if mapping[A[2][i]] != -1:
                    if mapping[A[2][i]] == x and first(i-1, s//10): return True
                else:
                    if not (mapped[x] or not x and not_zero[A[2][i]]):
                        mapping[A[2][i]] = x
                        mapped[x] = True

                        if first(i-1, s//10): return True
                        else:
                            mapping[A[2][i]] = -1
                            mapped[x] = False

                mapping[A[1][i]] = -1
                mapped[j] = False

            return False

    if first(N-1, 0):
        ret = [''.join([str(mapping[ai[j]]) for j in range(N) if ai[j] != -1]) for ai in A]

    return ret


if __name__ == '__main__': main()
