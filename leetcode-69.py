def mySqrt(x: int) -> int:
    a = 0
    while a*a <= x:
        a +=1
    return a-1

def mySqrt(x: int) -> int: # binary search
    if x <2:
        return x
    left = 0
    right = x
    while left <= right:
        mid = (left+right)//2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid +1
        else:
            right = mid -1
    return right

x = 11
res= mySqrt(x)
print(res)