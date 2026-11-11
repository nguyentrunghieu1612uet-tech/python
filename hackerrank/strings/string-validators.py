# HackerRank - string validators: https://www.hackerrank.com/challenges/string-validators/problem
# Ý tưởng: Dùng hàm any() để kiểm tra tất cả phần tử nếu có ít nhất 1 phần tử true thì trả về true

if __name__ == '__main__':
    s=input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))