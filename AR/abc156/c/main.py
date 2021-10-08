n = int(input())
x = list(map(int, input().split()))
def cost(xi, p):
    return (xi - p)**2
ans = 100*(100**2) + 1
for i in range(1, 101):
    tmp = sum([cost(xi, i) for xi in x])
    if tmp < ans: ans = tmp
print(ans)