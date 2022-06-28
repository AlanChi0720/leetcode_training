def longestCommonPrefix(strs: list[str]) -> str:
    common=""
    for i in range(len(strs[0])): # choose each character in each str
        for n in strs: # choose each str 
            if i == len(n) or n[i] != strs[0][i]:
                return common
        common += strs[0][i]
    return common

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))