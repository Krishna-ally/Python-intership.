"""MAGIC STRING

Description

Eva has a string S containing lowercase English letters. She wants to transform this string into a Magic String, where all the
characters in the string are the same. To do so, she can replace any letter in the string with another letter present in that string.
Your task is to help Eva find and return an integer value, representing the minimum number of steps required to form a Magic
String. Return 0, if S is already a Magic String.

Input Specification:
input1: A string S, containing lowercase English letters.

Output Specification:
Return an integer value, representing the minimum number of steps required to form a Magic String. Return 0, if S is already a
Magic String.

Sample Input:
aaabbbccdddd

Sample Output:
8

Source Code:"""

s=input()
n=len(s)
d={}
mx=0
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    if d[i]>mx:
        mx=d[i]
print(n-mx)
