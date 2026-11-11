# HackerRank - alphabet rangoli: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    d=size*4-3
    for i in range (size-1,-1,-1):
        l=[chr(97+j) for j in range(size-1,i-1,-1)]+[chr(97+j) for j in range(i+1,size,1)]
        l="-".join(l)  
        print(l.center(d,"-"))
    for i in range (1,size):
        l=[chr(97+j) for j in range(size-1,i-1,-1)]+[chr(97+j) for j in range(i+1,size,1)]
        l="-".join(l)  
        print(l.center(d,"-"))           
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)