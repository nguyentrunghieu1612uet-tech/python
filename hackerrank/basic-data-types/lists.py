"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each 
command will be of the 7 types listed above. Iterate through each command in order and perform 
the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range(N):
        command=input().split()
        cmd=command[0]
        nums=list(map(int,(command[1:])))
        if cmd=='insert':
            arr.insert(nums[0],nums[1])
        elif cmd=='print':
            print(arr)
        elif cmd=='remove':
            arr.remove(nums[0])
        elif cmd=='append':
            arr.append(nums[0])
        elif cmd=='sort':
            arr.sort()
        elif cmd=='pop':
            arr.pop()
        elif cmd=='reverse':
            arr.reverse()