def main():
    S = [input() for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                A, C = i+1, j+1
                break
        else: continue
        break

    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if S[i][j] == '#':
                B, D = i+1, j+1
                break
        else: continue
        break

    print(A, B)
    print(C, D)


if __name__ == '__main__': main()
