# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np
import sys
sys.setrecursionlimit(10**4)
S = input()
alpha = {chr(ord('a')+i) for i in range(26)}


def solve(s):
    if not s: return np.zeros(26, dtype=np.uint64)

    elif s[0] in alpha: return np.array([int(s[0] == chr(ord('a')+i)) for i in range(26)], dtype=np.uint64) + solve(s[1:])

    elif s[0] in '0123456789':
        n = ''
        for i in range(len(s)):
            if s[i] in '0123456789': n += s[i]
            else: break

        if s[i] in alpha:
            tmp = s[i]
            j = i
        else:
            tmp = ''
            cnt = 1
            for j in range(i+1, len(s)):
                if s[j] == '(': cnt += 1
                elif s[j] == ')': cnt -= 1

                if cnt: tmp += s[j]
                else: break

        return int(n)*solve(tmp) + solve(s[j+1:])


ans = solve(S)
_ = [print(chr(ord('a')+i), ans[i]) for i in range(26)]
