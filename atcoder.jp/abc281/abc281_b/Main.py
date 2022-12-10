from string import ascii_uppercase as up


def main():
    S = input()

    if len(S) != 8 or S[0] not in up or S[-1] not in up: ans = 'No'
    else:
        for i in range(100000, 1000000):
            if S[0] + str(i) + S[-1] != S: continue

            ans = 'Yes'
            break
        else: ans = 'No'

    print(ans)


if __name__ == '__main__': main()
