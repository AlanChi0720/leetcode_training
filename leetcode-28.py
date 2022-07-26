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
    if not needle: # if needle == 0 if needle == none:
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

def strStr(haystack: str, needle: str) -> int:
    # KMP algorithm
    if needle == "": return 0
    lps = [0] * len(needle)
    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS +1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS -1]
    
    i = 0 # for hay
    j = 0 # for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif haystack[i] != needle[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j -1]
        if j == len(needle):
            return i - len(needle)
    return -1

haystack = "hello"
needle = "ll"
# haystack = "aaaaa"
# needle = "baa"
res = strStr(haystack, needle)
print(res)