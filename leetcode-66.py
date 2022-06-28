def plusOne(digits: list[int]) -> list[int]:
    digits= digits[::-1]
    one, i= 1, 0
    while one == 1:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] =0
                one = 1
            else: # first digit is not 9 will does into this if and end
                digits[i] +=1
                one = 0
        else:
            digits.append(1)
            one=0
        i+=1
    return digits[::-1]

# def plusOne(digits: list[int]) -> list[int]:
#     return [digit for digit in str(int("".join(str(digit) for digit in digits))+1)]

digits = [8,9]
res= plusOne(digits)
print(res)
