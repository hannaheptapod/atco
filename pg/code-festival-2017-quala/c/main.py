from collections import Counter


def main():
    H, W = map(int, input().split())
    A = Counter()
    for _ in range(H):
        for aij in input(): A[aij] += 1

    cnt = Counter(A.values())
    unu = sum([v for k, v in cnt.items() if k%2])
    di = sum([2*v for k, v in cnt.items() if k%4 == 2])

    if H%2 == 0 and W%2 == 0: ans = 'Yes' if unu == 0 and di == 0 else 'No'
    elif H%2 and W%2: ans = 'Yes' if unu == 1 and di < H+W else 'No'
    elif H%2: ans = 'Yes' if unu == 0 and di <= W else 'No'
    else: ans = 'Yes' if unu == 0 and di <= H else 'No'

    print(ans)


if __name__ == '__main__': main()
