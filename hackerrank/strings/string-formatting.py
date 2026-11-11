# HackerRank - string formatting: https://www.hackerrank.com/challenges/python-string-formatting/problem
# Ý tưởng: Sử dụng biến w để tính độ rông. Sau đó sử dụng cú pháp f'{i:{w}d}', f'{i:{w}o}', f'{i:{w}X}', f'{i:{w}b}'

def print_formatted(number):
    # your code goes here
    w=len(f'{number:b}')
    for i in range (1,number+1,1):
        print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}") 
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)