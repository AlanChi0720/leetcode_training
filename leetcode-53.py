# def maxSubArray(nums: list[int]) -> int: 
    # maxsum = nums[0]
    # cursum= 0
    # for i in nums:
    #     if cursum <0:
    #         cursum =0
    #     cursum += i
    #     maxsum = max(maxsum, cursum)
    # return maxsum

def maxSubArray(nums):
    currSum = 0
    maxSum = nums[0]
    for n in nums :
        if currSum < 0 :
            currSum = 0
        currSum+=n
        if currSum > maxSum :
            maxSum = currSum
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
res= maxSubArray(nums)
print(res)