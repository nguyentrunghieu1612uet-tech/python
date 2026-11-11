# HackerRank - https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    s=s.split(' ')
    a=[x.capitalize() for x in s]
    a=' '.join(a)
    return a
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
