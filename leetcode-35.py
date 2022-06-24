# def searchInsert(nums: list[int], target: int) -> int:
#     for i in nums:
#         if target <= i:
#             return nums.index(i)
#         elif i < target <= i+1:
#             return nums.index(i)+1
#     return len(nums)

def searchInsert(nums: list[int], target: int) -> int:
    l=0
    r=len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            r= (l+r)//2 -1
        else:
            l=(l+r)//2 +1
    return l

nums = [1,3,5,6]
# target = 5
# target = 2
target = 7
res = searchInsert(nums,target)
print(res)