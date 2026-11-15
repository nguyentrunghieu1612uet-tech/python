# HackerRank - the minion game: https://www.hackerrank.com/challenges/the-minion-game/problem
# Ý tưởng: Kiểm tra từng kí tự xem nó là nguyên âm hay phụ âm và đếm số chuỗi bắt đầu từ điểm đó.

def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    for i in range (len(string)):
        if string[i] in ['U','E','O','A','I']:
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i
    if stuart > kevin:
            print (f"Stuart {stuart}")
    elif kevin > stuart:
            print (f"Kevin {kevin}")
    else:
            print ("Draw")
        
            
        
if __name__ == '__main__':
    s = input()
    minion_game(s)