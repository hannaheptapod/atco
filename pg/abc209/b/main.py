n, x = map(int, input().split())
a = list(map(int, input().split()))
a_1 = [a[i] - (i%2) for i in range(n)]
ans = 'Yes'
if sum(a_1) > x:
    ans = 'No' 
print(ans)