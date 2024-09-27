"""ENCODE THE NUMBER

Description

You work in the message encoding department of a national security agency. Every message that is sent from or received in
your office is encoded. You have an integer N, and each digit of N is squared and the squares are concatenated together to
encode the original number. Your task is to find and return an integer value representing the encoded value of the number.
input1: An integer value N representing the number to be encoded.

Output :
Return an integer value representing the encoded value of the number.

Sample Input:
167

Sample Output:
13649

Source Code:"""
    
n=int(input ())
res=0
f=1
while n>0:
    rem=n%10
    sq=rem**2
    if sq<10:
        res=sq*f+res
        f*=10
    else:
        res+=sq*f
        f*=100
    n//=10
print (res)
