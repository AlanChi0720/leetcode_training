# def addBinary(a: str, b: str) -> str:
#     newa= []
#     for i in a[::-1]:
#         newa.append(int(i))
#     newb= []
#     for i in b[::-1]:
#         newb.append(int(i))
#     added=[0,0]
#     n,m=0,0
#     while n < len(newa) or m < len(newb):
#         if newa[n]+ newb[m]+ added[n+1]== 0:
#             n +=1
#             m +=1
#             added.append(0)
#         elif newa[n]+ newb[m] +added[n+1]== 1:
#             n +=1
#             m +=1
#             added.append(1)
#         elif newa[n]+ newb[m] +added[n+1]== 2:
#             n +=1
#             m +=1
#             added.append(0)
#         else:
#             n +=1
#             m +=1
#             added.append(1)

#     print(added[::-1].pop())
#     return added

def addBinary(a: str, b: str) -> str:
    res = ""
    carry = 0
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry: # carry != 0
        res = "1" +res
    return res

a = "1010"
b = "1111"
res=addBinary(a,b)
print(res)