from typing import List
import math


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         if len(piles) == 1:
#             if piles[0] % h != 0:
#                 extra = 1
#             else:
#                 extra = 0
#             return piles[0] // h + extra
#         else:
#             l, r = 1, max(piles)
#             pilesize = 0
#             while l <= r:
#                 trysize = ((r - l) // 2) + l
#                 print(f"{l} {r}")
#                 time = 0
#                 for pile in piles:
#                     if pile % trysize != 0:
#                         time += 1
#                     time += pile // trysize
#                 print(f"trysize {trysize} time {time}")
#                 if time <= h:
#                     pilesize = trysize
#                     r = trysize - 1
#                 else:
#                     l = trysize + 1
#             return pilesize


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


piles = [1000000000]
h = 2

sol = Solution()
print(sol.minEatingSpeed(piles, h))
