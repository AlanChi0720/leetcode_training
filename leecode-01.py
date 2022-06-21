class Solution:
    def twosum(self, nums: list[3,1,5,2], target: 4) -> list[int]:
        prevMap = {}
        for i , n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
        return
Solution()