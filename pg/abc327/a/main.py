def main():
    N = int(input())
    S = input()

    ans = check(N, S)
    print(ans)


def check(N, S):
    for i in range(N-1):
        if S[i:i+2] in ['ab', 'ba']: return 'Yes'

    return 'No'


if __name__ == '__main__': main()
