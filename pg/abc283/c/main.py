def main():
    S = input()

    idx = 0
    ans = 0
    while idx < len(S):
        if idx + 1 < len(S) and S[idx:idx+2] == '00': idx += 2
        else: idx += 1

        ans += 1

    print(ans)


if __name__ == '__main__': main()
