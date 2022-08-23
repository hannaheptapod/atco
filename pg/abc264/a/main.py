"""
Problem Statement
Print the 
L
L-th through 
R
R-th characters of the string atcoder.
"""

L, R = map(int, input().split())
print(input()[L-1:R])
