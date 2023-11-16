def main():
    B = int(input())

    ans = solve(B)
    print(ans)


def solve(B):
    for a in range(1, 100):
        if a**a > B: return -1
        if a**a == B: return a
    return -1


if __name__ == '__main__': main()
