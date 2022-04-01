from itertools import combinations
sm = [sum(nums) for nums in combinations(map(int, input().split()), 3)]

ans = sorted(sm)[-3]
print(ans)
