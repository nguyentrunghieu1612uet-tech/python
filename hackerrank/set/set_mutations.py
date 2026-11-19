# HackerRank - Set mutations: https://www.hackerrank.com/challenges/py-set-mutations/problem

a=int(input())
A=set(map(int,input().split()))
n=int(input())
for _ in range(n):
    command=input().split()
    cmd=command[0]
    s=set(map(int,input().split()))
    if cmd=="update":
        A.update(s)
    elif cmd=="intersection_update":
        A.intersection_update(s)
    elif cmd=="difference_update":
        A.difference_update(s)
    elif cmd=="symmetric_difference_update":
        A.symmetric_difference_update(s)
print(sum(A))