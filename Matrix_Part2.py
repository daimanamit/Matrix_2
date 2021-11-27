
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:05:09 2019

@author: amit daiman
"""
A = [[11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]]
Symmetric = True
for x in range(len(A)):
    for y in range(len(A[x])):
        if A[x][y] != A[y][x]:
            Symmetric = False
            break
        print("A is NON-SYMMETRIC")
    if not Symmetric:
        break
        print("A is SYMMETRIC")
