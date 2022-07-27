class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))

        for i in mag:
            if ran and i == ran[0]:
                ran.pop(0)
        if ran:
            return False
        else:
            return True

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = collections.Counter(magazine)
        for char in ransomNote:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
                if dic[char] < 0:
                    return False
        return True

ransomNote = ""
magazine = "b"
ans = Solution().canConstruct(ransomNote,magazine)
print(ans)