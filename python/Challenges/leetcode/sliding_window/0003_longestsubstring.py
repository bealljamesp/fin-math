class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        lstring = []
        for c in s:
            if c not in lstring:
                lstring.append(c)
            else:
                lstring.append(c)
                lstring = lstring[lstring.index(c) + 1 :]
            if len(lstring) > res:
                res = len(lstring)
        return res


s = "tmmzuxt"
# output = 5

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
