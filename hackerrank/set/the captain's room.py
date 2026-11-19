# HackerRank - the captain's room: https://www.hackerrank.com/challenges/py-the-captains-room/problem

K=int(input())
number_list=list(map(int,input().split()))
number_set=set(number_list)
x=sum(number_set)-((sum(number_list)-sum(number_set))//(K-1))
print(x)