def main():
    global S, X, Y
    S = input()
    X, Y = map(int, input().split())

    ans = solve()
    print(ans)


def solve():
    lens = tuple(len(si) for si in S.split('T'))
    movs = [[0], [0]]
    for i, l in enumerate(lens[1:]): movs[1 - i%2].append(l)

    return 'Yes' if knapsack(movs[0], X-lens[0]) and knapsack(movs[1], Y) else 'No'


def knapsack(mov, goal):
    goal = abs(goal)
    sm = sum(mov)
    tar = (sm - goal)//2
    if tar < 0 or sm-2*tar != goal: return False

    dp = [False]*(1<<15)
    dp[0] = True
    for m in mov:
        for i in range(tar-m+1):
            if not dp[i]: continue
            dp[i+m] = True
            if i+m == tar: break
        else: continue
        break

    return dp[tar]


if __name__ == '__main__': main()
