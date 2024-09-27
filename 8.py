"""BEST GRADE

Description

Andrew has a string N consisting of lowercase English letters representing respective grades of N students in his class. His grade is at
Pth index. He can swap any two adjacent grades.
Your task is to help Andrew find and return a string value, representing maximized grade by bringing lexicographically smallest
character on the Pth index after doing at most K swaps

Note: use 1 based indexing.

Input format:
(i) The first line contains the string s.
(ii) The second line contains the integer P.
(iii) The third line contains the integer K.

Sample Input:

abcdefg
3
2

Sample Output:
a

Source Code:"""
    
a=input()
p=int(input())
k=int(input())
s=max(0,p-k-1)
e=min(len(a),p+k)
print(min(a[s:e]))
