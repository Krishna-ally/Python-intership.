"""OBJECT SCORE

Description


In a family, there are N members each have a capacity of Ci units to buy anything. In a store there are M objects. Each
of which have some price Pi and weight Wi print on it. Each of the members go to the store and can buy all those
items whose price is less than or equal to their buying capacity and store that bought object in a bag. Find the
maximum weight of each of the bags collected by all N members individually.

Input Format:
First line contains two integers N and M where N is the number of members in the house and M is the number of
objects in the store.
Second line contains N space-separated integers (C1, C2, C3,...)
the next M lines contains each object price and weight(Pi,Wi) as space seperated integers.

Sample Input:

3 4
10 20 30
5 10
15 20
10 25
20 30

Sample Output:
35 85 85

Source Code:"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
p=[]
for j in range(m):
    price,weight=list(map(int,input().split()))
    p.append([price,weight])
res=[]
for i in a:
    t=0
    for prc,wt in p:
        if prc<=i:
            t+=wt
    res.append(t)
print(*res,sep=" ")
