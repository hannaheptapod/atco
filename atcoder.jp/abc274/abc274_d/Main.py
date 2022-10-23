def main():
    global N, X, Y, A
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    ans = calc()
    print('Yes' if ans else 'No')


def calc():
    hor, ver = A[::2] + [0], A[1::2]  # x方向の移動horについては，len(hor[1:]) > 0 となるよう0を追加
    sm_h, sm_v = sum(hor[1:]), sum(ver)

    """
    進む距離と戻る距離の偶奇が一致した場合は，和差算により得られた整数解についてナップザック問題を解く
    x方向の移動horについては A[0] -> X への移動を考える
    """
    if sm_h%2 != (X - A[0])%2 or sm_v%2 != Y%2: return False
    else: return knapsack(hor[1:], (X - A[0] + sm_h)//2) and knapsack(ver, (Y + sm_v)//2)


def knapsack(arr, w):
    dp = [True] + [False]*(10**4 + 10)  # ナップザックの容量をケチらない！

    for ai in arr:
        for j in range(w+1):
            if dp[j]: dp[j+ai] = True
            if dp[w]: return True
    return dp[w]


if __name__ == '__main__': main()
