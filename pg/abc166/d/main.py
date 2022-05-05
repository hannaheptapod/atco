X = int(input())

for a in range(-200, 201):
    tmp = a**5

    for b in range(-200, 201):
        if tmp - b**5 == X: break
    else: continue
    break

print(a, b)
