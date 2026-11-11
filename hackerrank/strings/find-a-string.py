# HackerRank - find a string: https://www.hackerrank.com/challenges/find-a-string/problem
# Ý tưởng: dùng vòng lặp for để chạy kiểm tra
def count_substring(string, sub_string):
    if len(string)<len(sub_string): return 0
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)