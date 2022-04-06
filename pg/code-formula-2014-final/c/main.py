S = input() + ' '

st = set()
tmp = ''
flag = False

for si in S:
    if flag:
        if si == ' ':
            if tmp:
                st.add(tmp)
                tmp = ''

            flag = False

        elif si == '@':
            if tmp:
                st.add(tmp)
                tmp = ''

        else: tmp += si

    elif si == '@': flag = True

print(*sorted(st), sep='\n')
