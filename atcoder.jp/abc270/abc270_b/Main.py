def main():
    X, Y, Z = map(int, input().split())

    if X*Y < 0 or abs(X) < abs(Y): ans = abs(X)
    elif Z*Y < 0: ans = abs(X) + 2*abs(Z)
    elif abs(Z) < abs(Y): ans = abs(X)
    else: ans = -1

    print(ans)


if __name__ == '__main__': main()
