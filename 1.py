"""
ADVACED SUB ARRAY PROBLEM

Description
You are competing in a basketball contest. In this contest the score for each successful shot depends on both the distance from
the basket and the player's position. The ball is shot N times, successfully. You are given an array A containing the distance of a
player from basket for N shots. The index of array represents the position of the player. Score is calculated by multiplying the
position with the distance from the basket.
Your task is to find and return an integer value, representing the maximum possible score you can achieve by choosing a
contiguous subarray of size K from the given array.

Note:
* A subarray is a contiguous part of array.
* Assume 1 based indexing.
* The array contains both negative and positive values.
* Assume the player is standing on a cartesian plane.

Input Format
- input1:An integer value N representing the number of shots made by the player
- input2 : An integer K representing the size of subarray
- input3 : An array of integers

Sample Input
5
2
1 2 3 4 5

Sample Output
14

Source Code:"""

goal= int(input())
size=int(input())
l=list(map(int,input().split()))
x=0
for i in range (0,len(l)):
    sub=l[i:i+size]
    k=1
    s=0
    for j in sub:
        s+=(j*k)
        k+=1
        if s>x:
            x=s
print(x)
