"""PEAK ELEMENT FINDER

Description:

Description: You are given an N- dimensional array arr[]. A peak element in the array is defined as an element whose value is greater
than or equal to its neighboring elements (if they exist). Your task is to find the index of any peak element in the given array

Note: use 0-based indexing

Input:
An integer representing the number of elements in the array. N space-separated integers, denoting the elements of the array.
N space-separated integers ,denoting the elements of the array arr[]

Sample Input:
5
1 3 20 4 1

Sample Output:
2

Source Code:"""

n=int(input())
l=list(map(int,input().split()))
mx=0
for i in range(0,n):
    if i==0:
        if l[i]>l[i+1]:
            mx=i
            break
    elif i==(len(l))-1:
        if l[i]>=l[i-1]:
            mx=i
            break
    else:
        if l[i]>=l[i+1] and l[i]>=l[i-1]:
            mx=i
            break
print(mx)
