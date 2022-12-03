def main():
    S, T = input(), input()

    for i, si in enumerate(S):
        if si != T[i]:
            ans = i+1
            break
    else: ans = len(S)+1

    print(ans)


if __name__ == '__main__': main()
