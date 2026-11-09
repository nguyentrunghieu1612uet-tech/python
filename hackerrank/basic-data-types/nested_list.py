"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    second=sorted(set(r[1] for r in record))
    slg=second[1]
    name=sorted([r[0] for r in record if r[1]==slg])
    for _ in name:
        print(_)