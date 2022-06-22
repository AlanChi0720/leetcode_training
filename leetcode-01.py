# def twosum(nums, target):
#     prevMap = {}
#     for i , n in enumerate(nums):
#         diff = target - n 
#         if diff in prevMap:
#             return [prevMap[diff], i]
#         prevMap[n]=i
#     return 


def twosum(nums, target):
    keymap={}
    for i in range(len(nums)):
        if target - nums[i] in keymap:
            return [keymap[target-nums[i]],i]
        if nums[i] not in keymap:
            keymap[nums[i]] = i

nums= [2,3,5,7,11,13]
target=9
print(twosum(nums,target))