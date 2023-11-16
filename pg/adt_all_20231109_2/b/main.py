def main():
    S = input()

    if int(S[-1]) <= 2: print(S[:-2] + '-')
    elif int(S[-1]) <= 6: print(S[:-2])
    else: print(S[:-2] + '+')


if __name__ == '__main__': main()
