# HackerRank - no idea!: https://www.hackerrank.com/challenges/no-idea/problem

m,n=map(int,input().split())
array=list(map(int,input().split()))
A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))
point=0
for i in array:
    if i in A:
        point+=1
    if i in B:
        point-=1
print(point)