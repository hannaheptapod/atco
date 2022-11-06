def main():
    S = input()

    ans = -1
    for i, s in enumerate(S[::-1]):
        if s == 'a':
            ans = len(S)-i
            break

    print(ans)


if __name__ == '__main__': main()
