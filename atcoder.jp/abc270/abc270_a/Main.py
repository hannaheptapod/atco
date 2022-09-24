def main():
    A, B = map(int, input().split())

    ans = 0
    if A%2 or B%2: ans += 1
    if A%4 >= 2 or B%4 >= 2: ans += 2
    if A >= 4 or B >= 4: ans += 4
    print(ans)


if __name__ == '__main__': main()
