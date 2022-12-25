def main():
    S = input()

    dic = {}
    arr_l, cnt = [], 0
    for i, si in enumerate(S):
        if si == '(':
            cnt += 1
            arr_l.append(i)
        elif si == ')':
            cnt -= 1
            delete = set()
            for k, v in dic.items():
                if arr_l[cnt] < v: delete.add(k)
            for k in delete: del dic[k]
        else:
            if si in dic:
                ans = 'No'
                break
            else: dic[si] = i
    else: ans = 'Yes'

    print(ans)


if __name__ == '__main__': main()
