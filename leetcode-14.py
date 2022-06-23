def longestCommonPrefix(strs: list[str]) -> str:
    common=""
    for i in range(len(strs[0])):
        for n in strs:
            if i == len(n) or n[i] != strs[0][i]:
                return common
        common += strs[0][i]
    return common

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))