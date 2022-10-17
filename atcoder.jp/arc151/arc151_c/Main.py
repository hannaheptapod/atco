from bisect import insort


def main():
    N, M = map(int, input().split())
    arr = [[0, -1], [N+1, -1]]
    for _ in range(M): insort(arr, list(map(int, input().split())))

    xor = 0
    for i in range(M+1):
        if arr[i][1] == arr[i+1][1] == -1: xor ^= N%2
        elif min(arr[i][1], arr[i+1][1]) == -1: xor ^= arr[i+1][0] - arr[i][0] - 1
        elif arr[i][1] == arr[i+1][1]: xor ^= 1
        else: xor ^= 0

    print('Takahashi' if xor else 'Aoki')


if __name__ == '__main__': main()
