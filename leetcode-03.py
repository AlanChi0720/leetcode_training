class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chartset = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in chartset:
                chartset.remove(s[l])
                l += 1
            chartset.add(s[i])
            res = max(res, i-l+1)
        return res

s = "pwwkew"
ans = Solution().lengthOfLongestSubstring(s)
print(ans)