"""SIGNATURE FOR LCM


Description
Given two numbers a and b. Find the GCD and LCM of and b.

Input:
• Two positive integers a and b (1 <=a, b <=1000)

Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b

Sample Input:
12 18

Output:
6
36

Explanation:
The GCD of 12 and 18 is 6. The LCM of 12 and 18 is 36.

Source Code:"""

import math
a,b=list(map(int,input().split()))
def lcm(a,b):
    return (a*b)//math.gcd(a,b)
print(math.gcd(a,b))
print(lcm(a,b))
