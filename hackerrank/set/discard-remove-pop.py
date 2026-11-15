# HackerRank: discard-remove-pop: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    command=input().split()
    cmd=command[0]
    if cmd== 'pop': 
        s.pop()
    if cmd== 'remove':
        s.remove(int(command[1]))
    if cmd== 'discard':
        s.discard(int(command[1]))
print(sum(s))