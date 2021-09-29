a, b = map(int, input().split())
num = b
if num < 10:
    num += 10 * a
elif num < 100:
    num += 100 * a
else:
    num += 1000 * a
ans = 'No'
for i in range(1, 400):
    if i**2 == num:
        ans = 'Yes'
        break
print(ans)