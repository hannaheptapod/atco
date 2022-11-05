def main():
    S = input()

    ans = -1
    for i, s in enumerate(S):
        if s == 'a': ans = i+1

    print(ans)


if __name__ == '__main__': main()
