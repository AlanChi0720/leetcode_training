class Solution:
    def generateParenthesis(self, n: int) :
        stack = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN +1, closeN)
                print(stack)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN +1)
                stack.pop()
        backtrack(0,0)
        return res

n = 2
ans = Solution().generateParenthesis(n)
print(ans)