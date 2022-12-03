def main():
    global K
    K = int(input())

    facts = factorization(K)

    ans = max(binary_search(p, c) for p, c in facts)
    print(ans)


def factorization(n):
    arr = []
    temp = n

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0

            while temp%i == 0:
                cnt += 1
                temp //= i

            arr.append([i, cnt])

    if temp != 1: arr.append([temp, 1])
    if arr==[]: arr.append([n, 1])

    return arr


def binary_search(p, c):
    ok, ng = 10**12, 1

    def is_ok(x, p, c):
        cnt = 0
        while x:
            x //= p
            cnt += x

        return cnt >= c

    while abs(ok-ng) > 1:
        md = (ok+ng)//2

        if is_ok(md, p, c): ok = md
        else: ng = md

    return ok


if __name__ == '__main__': main()
