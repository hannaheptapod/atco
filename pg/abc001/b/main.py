m = int(input())
km = m / 1000
vv = 0
if m <= 100 and m <= 5000:
    vv = 10 * km
elif km >= 6 and km <= 30:
    vv = km + 50
elif km >= 35 and km <= 70:
    vv = (km - 30) / 5 + 80
else:
    vv = 89
print('{:02}'.format(int(vv)))