def main():
    N = int(input())
    s = '0123456789ABCDEF'

    ans = s[N//16]+s[N%16]
    print(ans)


if __name__ == '__main__': main()
