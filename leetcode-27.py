def removeElement( nums: list[int], val: int) -> int:
    l = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l] =nums[i]
            l += 1
    return l , nums


nums = [0,1,2,2,3,0,4,2]
val = 2
res= removeElement(nums,val)
print(res)