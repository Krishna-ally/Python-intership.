"""TARGET SUM

Description

You are given a list of integers, and your task is to write a function that finds the two numbers in the list that add up to a
specific target sum. You need to retum the indices of these two numbers.
Write a function that takes a list of Integers and a target sum as input and returns a list of two indices (0-based) of the numbers
that add up to the target sum. Assume that there is exactly one solution, and you cannot use the same element twice

Sample Input:

2 7 11 15
9

Sample Output:
[0, 1]

Source Code:"""

l=list(map(int,input().split()))
s=int(input())
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l [i]+l[j]==s:
            ans.append(i)
            ans.append(j)
print(ans)
