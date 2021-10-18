ps = input()
p = [int(ps[i]) for i in range(4)]
d = [p[i+1] + 10 - p[i] for i in range(3)]
if all(di == 10 for di in d) or all((di%10) == 1 for di in d):
    print('Weak')
else:
    print('Strong')