def main():
    K = int(input())

    ans = ''.join(chr(ord('A') + i) for i in range(K))
    print(ans)


if __name__ == '__main__': main()
