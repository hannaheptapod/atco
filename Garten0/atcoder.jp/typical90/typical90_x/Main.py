n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
diff = [abs(a[i] - b[i]) for i in range(n)]
d = sum(diff)
ans = 'No'
if d <= k and (d - k) % 2 == 0:
    ans = 'Yes'
print(ans)