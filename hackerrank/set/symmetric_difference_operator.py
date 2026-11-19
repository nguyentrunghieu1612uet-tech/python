# HackerRank - symmetric_difference_operator: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

m=int(input())
a=set(list(map(int,input().split())))
n=int(input())
b=set(list(map(int,input().split())))
print(len(a^b))