def climbStairs(n: int) -> int: # dynamic programming solution 
    oneBack=1
    twoBack=1
    if n <= 1: return 1
    for i in range(2, n+1):
        cur=oneBack+twoBack
        twoBack=oneBack
        oneBack=cur
    return oneBack

def climbStairs(n: int) -> int: # dynamic programming solution 2
    dp = [1, 1]
    for i in range(2, n + 1):
        dp.insert(i, dp[i - 1] + dp[i - 2])
    return dp[n]

def climbStairs(n: int) -> int: # Top down memoization: backtracking
    cache={}
    def helper(n):
        if n in cache: return cache[n]
        if n == 0 or n == 1: return 1
        cache[n] = helper(n-1) + helper(n-2)
        return cache[n]
    return helper(n)

# solution  URL = https://leetcode.com/problems/climbing-stairs/discuss/861070/Progression-of-python-solutions

n = 5
res = climbStairs(n)
print(res)