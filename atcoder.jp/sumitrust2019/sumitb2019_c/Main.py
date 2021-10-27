x = int(input())
m = x // 100
n = -int(-(x%100 / 5) // 1)
print(int(m >= n))