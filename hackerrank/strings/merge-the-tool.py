# HackerRank - merge the tool: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Ý tưởng: Tạo ra các chuỗi a có độ dài k sau khi chia. Tạo chuỗi rỗng u kiểm tra từng kí tự trong a nếu khác thì cập nhật thêm kí tự chào chuỗi.

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        a=string[i:i+k]
        u=''
        for j in range (len(a)):
            if a[j] not in u:
                u+=(a[j])
        print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)