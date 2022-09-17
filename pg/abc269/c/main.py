from itertools import product


def main():
    N = bin(int(input()))[2:]
    arr = [len(N)-i-1 for i in range(len(N)) if N[i] == '1']

    ans = set()
    for bits in product([0, 1], repeat=len(arr)):
        tmp = 0
        for i in range(len(arr)):
            tmp += bits[i] * (2**arr[i])
        ans.add(tmp)

    ans = sorted(ans)
    print(*ans, sep='\n')


if __name__ == '__main__': main()
