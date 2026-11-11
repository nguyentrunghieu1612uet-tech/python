#HackerRank - designer-door-mat: https://www.hackerrank.com/challenges/designer-door-mat/problem

n,m=map(int,input().split())
for i in range ((n-1)//2):
    print('-'*((m-3*(2*i+1))//2)+(2*i+1)*'.|.'+'-'*((m-3*(2*i+1))//2))
print ('-'*((m-7)//2)+'WELCOME'+'-'*((m-7)//2))
for i in range ((n-3)//2,-1,-1):
    print('-'*((m-3*(2*i+1))//2)+(2*i+1)*'.|.'+'-'*((m-3*(2*i+1))//2))