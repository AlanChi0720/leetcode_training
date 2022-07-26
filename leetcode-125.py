def isPalindrome(s: str) -> bool:
    newstr = ""
    for i in s:
        if i.isalnum():
            newstr += i.lower()
    return newstr == newstr[::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9"))

s = "0p"
ans = Solution().isPalindrome(s)
print(ans)