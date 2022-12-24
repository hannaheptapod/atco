def main():
    S = input()

    dic = {}
    arr_l, cnt_r = [], 0
    for i, si in enumerate(S):
        if si == '(': arr_l.append(i)
        elif si == ')':
            delete = set()
            for k, v in dic.items():
                if arr_l[cnt_r] < v: delete.add(k)
            for k in delete: del dic[k]
            cnt_r += 1
        else:
            if si in dic:
                ans = 'No'
                break
            else: dic[si] = i
    else: ans = 'Yes'

    print(ans)


if __name__ == '__main__': main()
