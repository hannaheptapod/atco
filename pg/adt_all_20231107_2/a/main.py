def main():
    L1, R1, L2, R2 = map(int, input().split())

    ans = max(min(R1, R2) - max(L1, L2), 0)
    print(ans)


if __name__ == '__main__': main()
