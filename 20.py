"""SUB ARRAY WITH MAX SUM

Description

You are given a list of integers, and your task is to find the subarray with the maximum sum. Write a function or method to
solve this problem efficiently and return the maximum sum.

Input:
n: the no of elements in the array
nums (List of integers): A list of integers (1 <= len(nums) <= 10^5)

Sample input:
8
-1 2 3 10 -4 7 2 -5

Sample output:
20

Explanation:
The max subarry sum is 20. The subarray is [2,3,10,-4,7,2]

Source Code:"""

n=int(input())
l=list(map(int,input().split()))
s=l[0]
ms=l[0]
for i in range(1,n):
    s=max(l[i],s+l[i])
    ms=max(ms,s)
print(ms)
