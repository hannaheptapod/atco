n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
diff = [abs(a[0] - b[0])]
i = j = 0
while (i < n) and (j < m):
    if a[i] < b[j]:
        if i == n - 1:
            diff.append(b[j] - a[i])
            break
        elif a[i + 1] > b[j]:
            diff.append(b[j] - a[i])
        i += 1
    elif b[j] < a[i]:
        if j == m - 1:
            diff.append(a[i] - b[j])
            break
        elif b[j + 1] > a[i]:
            diff.append(a[i] - b[j])
        j += 1
    elif a[i] == b[j]:
        diff.append(0)
        break
    else:
        continue
diff.sort()
print(diff[0])