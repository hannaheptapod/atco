def main():
    S, T = input(), input()

    lens, lent = len(S), len(T)

    ans = 'No'
    for i in range(lens - lent + 1):
        if S[i:i + lent] == T:
            ans = 'Yes'
            break

    print(ans)


if __name__ == '__main__': main()
