n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort(reverse=True)
x_diff = [x[i] - x[i + 1] for i in range(m - 1)]
x_diff.sort()
print(sum(x_diff[i] for i in range(m - n)))