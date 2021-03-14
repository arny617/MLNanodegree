# Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

# You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

# You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

# More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

# You stop eating when you encounter an empty wrapper.

# For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

# The goal is to count the number of chocolates that you will eat, following the above rules.

### Euclidean algorithm to find Greatest common divisor or HCF
def calcHCF(A,B):
    if(B==0):
        return A
    else:
        return calcHCF(B,A%B)

def chocolateByNum(N,M):
    lcm = N*M/calcHCF(N,M)
    return int(lcm/M) 
