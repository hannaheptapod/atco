a, b = map(int,input().split())
c = (a - b)/3 + b
if (a-b)%3 == 0:
    print(int(c))
else:
    print('{:9f}'.format(c))