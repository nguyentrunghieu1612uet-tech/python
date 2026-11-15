# HackerRank - symmetric difference: https://www.hackerrank.com/challenges/symmetric-difference/problem

m=int(input())
a=set(list(map(int,input().split())))
n=int(input())
b=set(list(map(int,input().split())))
for i in sorted(a.difference(b).union(b.difference(a))):
    print(i)