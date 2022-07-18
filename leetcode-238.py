class Solution:
    def productExceptSelf(self, nums):
        ans = [1] *(len(nums))
        prefix =1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans

solution = Solution()
nums = [1,2,3,4]
ans = solution.productExceptSelf(nums)
print(ans)