# HackerRank - check strict supset: https://www.hackerrank.com/challenges/py-check-strict-superset/problem\

def is_strict_superset(big, small):
    return all(x in big for x in small) and len(big) > len(small)

A = set(map(int, input().split()))
n = int(input())
print(all(is_strict_superset(A, set(map(int, input().split()))) for _ in range(n)))