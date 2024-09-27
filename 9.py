"""CANDIES

Description

Let's consider a scenario where there are K candies to be distributed among N children, each uniquely numbered from 1 to N.
The distribution commences with Child A, followed by a sequential allocation to the subsequent children in the order: A, A+1,
A+2,..., N. The query at hand is to identify which child will be the last recipient of a candy.
In more explicit terms, after Child x (where 1<= x < N) receives a candy, the subsequent candy is granted to Child x+1. Upon
Child N receiving a candy, the distribution cycle restarts. and Child 1 becomes the next recipient.
The primary objective is to ascertain the identity of the child who will receive the last candy in this cyclic distribution.
Note: Each child receives only 1 candy.

Input Format:

The first line of input contains 3 space seperated integers N, K and A.

Output Format:

Print the friend who will be the final recipient of the candy.

Constraints:
1<=N<=K<=10^8

Sample Input:
5 2 1

Sample Output:
2

Source Code:"""
    
n,k,a=list(map(int,input().split()))
ans=(a+k-1)%n
if ans==0:
    print(n)
else:
    print(ans)
