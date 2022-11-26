def main():
    S = input()

    dic = {'v': 1, 'w': 2}

    ans = 0
    for si in S: ans += dic[si]

    print(ans)


if __name__ == '__main__': main()
