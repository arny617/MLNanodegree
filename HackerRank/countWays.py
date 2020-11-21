def memoize(f):
    memo = {}
    def helper(S,m,n):
        if (m,n) not in memo:
            memo[m,n] = f(S,m,n)
        return memo[m,n]
    return helper
def count(S,m,n):
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0;   
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return count( S, m - 1, n) + count( S, m, n-S[m-1])
def getWays(n, c):
    # Write your code here
    m = len(c)
    countmem = memoize(count)
    return countmem(c,m,n)
