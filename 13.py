"""NUMBER OF COMBINATIONS LEADING TO A PRODUCT

Description

Problem Statement:

You are given an array arr and a product m. Your task is to find the number of possible unique triplets whose product of
elements is m.

Input Format:
The first line contains the integer, n
The second line contains space seperated integers of the array, arr
The third line contains the product m.
The input will be read from the STDIN by the candidate

Output Format:
The output consists of a single integer, i.e. the count of unique triplets having product m.
The output will be matched to the candidate's output printed on the STDOUT

Example:
Input:

7
5 3 20 10 1 4 2
60

Output:
3

Explanation:

Product m:60
Possible triplets for product m: (5,4,3),(20,3,1), (10,3,2)
The count of unique triplets is 3.

Source Code:"""

n=int(input())
l=list(map(int,input().split()))
p=int(input())
c=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range (j+1,n):
            if l[i]*l[j]*l[k]==p:
                c+=1
print (c)
