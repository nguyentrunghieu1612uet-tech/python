# HackerRank - sWAP cASE: https://www.hackerrank.com/challenges/swap-case/problem
# Ý tưởng: Chuyển các kí tự hoa thành kí tự thường và kí tự thường thành kĩ tự hoa còn kí tự không phải chữ cái giữ nguyên
def swap_case(s):
    result=''
    for i in range(len(s)):
        if 'a'<=s[i]<='z':
            result+=s[i].upper()
        elif 'A'<=s[i]<='Z':
            result+=s[i].lower()
        else:
            result+=s[i]
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)