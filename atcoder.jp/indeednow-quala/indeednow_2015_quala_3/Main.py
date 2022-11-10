def main():
    N = int(input())
    studs = sorted((i for i in (int(input()) for _ in range(N)) if i), reverse=True)
    Q = int(input())
    rooms = (int(input()) for _ in range(Q))

    leng = len(studs)
    for room in rooms: print(studs[room] + 1 if room < leng else 0)


if __name__ == '__main__': main()
