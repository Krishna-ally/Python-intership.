"""MISSING ALPHABETS

Description

Pangram is a sentence containing every letter in the English alphabet. Given a string, find all characters that are missing from
the string, Le., the characters that can make the string a Pangram We need to print output in alphabetic order.
For example,

Input: welcome to geeksforgeeks

Output: abdhijnpquvxyz

Source Code:"""
    
s=input()
a="abcdefghijklmnopqrstuvwxyz"
d=""
for i in a:
    if i not in s:
        d+=i
print(d)
