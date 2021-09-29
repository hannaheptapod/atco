a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
ans = "Yay!"
for i in [a, b, c, d, e]:
    for j in [a, b, c, d, e]:
        if abs(i - j) > k:
            ans = ":("
print(ans)