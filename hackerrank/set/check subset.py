# HackerRank - check subset: https://www.hackerrank.com/challenges/py-check-subset/problem

T=int(input())
for _ in range(T):
    a=int(input())
    A=set(map(int,input().split()))
    b=int(input())
    B=set(map(int,input().split()))
    print(all(x in B for x in A))