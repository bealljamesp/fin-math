from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        workinglist = []
        res = 0
        for c in s:
            workinglist.append(c)
            counts = Counter(workinglist)
            most_common, count = counts.most_common(1)[0]
            if len(workinglist) - count > k:
                workinglist = workinglist[1:]
        return len(workinglist)


s = "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
k = 7

sol = Solution()
print(sol.characterReplacement(s, k))


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         counts = defaultdict(int)
#         left = 0
#         max_len = 0
#         max_count = 0
#         ans = 0
#         for right in range(len(s)):
#             counts[s[right]] += 1
#             max_count = max(max_count, counts[s[right]])
#             if right - left + 1 > max_count + k:
#                     counts[s[left]] -= 1
#                     left += 1

#             ans = right - left + 1
#         return ans


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         l = 0
#         d = {}
#         maxi = 0

#         for r in range(len(s)):

#             d[s[r]] = 1+d.get(s[r], 0)
#             maxi = max(maxi, d[s[r]])

#             while (r-l+1)-maxi>k:
#                 d[s[l]]-=1
#                 l+=1

#         return (r-l+1)
