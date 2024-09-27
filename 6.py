"""ELECTIONS

Description

You are the head of the election committee in your village. Each Political party is associated with a unique number and the
votes are represented as an integer array A. where each element contains the party number voted for by the villagers. For a
party to win, they must have a majority of votes. our task is to find and return an integer value denoting the winning party's
number. Return -1 if there is no party with a majority.

Note: If only one vote is there he is the winner.

Input Format :
input1: An integer value representing the number the number of voters
input2: An integer array A representing the votes of the voters.

output Format:
Return an integer value denoting the winning party's number.Return -1 there is no party with a majority

Example 1:

Input:
6
1 1 2 2 2 3

Output:
2

Explanation:
As 2 got the most number of votes i.e 3.

Example 2:

Input:
6
1 2 1 1 2 2

Output:
-1

Explanation:

As both the contestants got same votes there is no majority.

Source Code:"""

n=int(input())
array=list(map(int,input().split()))
d={}
if n==1:
    print(array[0])
else:
    for i in array:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    x=sorted(d.items(),key=lambda x:x[1],reverse=True)
if x[0][1]==x[1][1]:
    print(-1)
else:
    print(x[0][0])
