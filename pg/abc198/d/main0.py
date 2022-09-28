from itertools import permutations


def main():
    S = [list(input()) for _ in range(3)]

    ans = solve(S)
    print(*ans, sep='\n')


def solve(s):
    st = set([sij for si in s for sij in si])

    ret = ['UNSOLVABLE']
    if len(st) <= 10 and len(s[2]) >= max(len(s[0]), len(s[1])):
        for p in permutations(range(10), len(st)):
            dic = {k: v for k, v in zip(st, p)}
            if not all(dic[si[0]] for si in s): continue

            abc = [0, 0, 0]
            for i in range(3):
                tmp = 0
                for sij in s[i]: tmp = tmp*10 + dic[sij]
                abc[i] = tmp

            if abc[0] + abc[1] == abc[2]:
                ret = abc
                break

    return ret


if __name__ == '__main__': main()
