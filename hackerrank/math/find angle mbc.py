# HackerRank - find angle mbc: https://www.hackerrank.com/challenges/find-angle/problem

import math
AB=float(input())
BC=float(input())
print(f"{int(math.degrees(math.atan2(AB,BC))+0.5)}{chr(176)}")