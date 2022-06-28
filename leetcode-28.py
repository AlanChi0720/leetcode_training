# def strStr(haystack: str, needle: str) -> int:
#     hay=[]
#     nee=[]
#     for i in haystack:
#         hay.append(i)
#         print(hay)
#     for n in needle:
#         nee.append(n)
#         print(nee)
#     while nee and hay:
#         if nee in hay:
#             index = hay.index(nee)
#             return index
#         else:
#             return -1
#     if not nee:
#         return 0

def strStr(haystack: str, needle: str) -> int:
    if not needle: # if needle == 0
        return 0
    if needle in haystack:
        index = haystack.index(needle)
        return index
    else:
        return -1

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    for i in range(len(haystack)+1 -len(needle)):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

haystack = "hello"
needle = "ll"
# haystack = "aaaaa"
# needle = "baa"
res = strStr(haystack, needle)
print(res)