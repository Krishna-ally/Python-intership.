"""REVERSE THE ORDER OF STRING

Description

You are given a string containing words separated by spaces. Your task is to write a function or program that reverses the order
of words in the string.

Sample Input:
Hello World

Sample Output:
World Hello

Source Code:"""

s=input().split()
print(*s[::-1])
