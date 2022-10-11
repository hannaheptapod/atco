def main():
    L, R = map(int, input().split())
    S = input()

    ans = ''.join([S[:L-1], S[R-1:L-2:-1] if L > 1 or R < len(S) else S[::-1], S[R:]])
    print(ans)


if __name__ == '__main__': main()
