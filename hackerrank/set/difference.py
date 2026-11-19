# HackerRank - set.difference() operation: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n=int(input())
N=set(map(int,input().split()))
b=int(input())
B=set(map(int,input().split()))
print(len(N.difference(B)))