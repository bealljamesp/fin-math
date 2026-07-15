# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:

#         l, r = 0, 0

#         lists1 = list(s1)
#         lists2 = list(s2)

#         while l <= len(s2) - len(s1):
#             if lists2[r] in lists1:
#                 lists1.remove(lists2[r])
#                 if len(lists1) == 0:
#                     return True
#                     break
#                 else:
#                     r += 1
#             else:
#                 lists1 = list(s1)
#                 l += 1
#                 r = l
#         return False


# s1 = "ab"  # True
# s2 = "eidbaooo"

# s1 = "ab" # False
# s2 = "eidboaoo"

# s1 = "adc" # True
# s2 = "dcda"


# Output: false

# sol = Solution()
# print(sol.checkInclusion(s1, s2))


# try two


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:

#         while s1[0] in list(s2):

#             lists1 = list(s1)
#             lists2 = list(s2)

#             for letter in lists1[1:]:

#                 l, r, count = 1, 1, 0

#                 if letter == lists2[lists2.index(s1[0]) - l]:
#                     l += 1
#                     count += 1
#                     continue

#                 elif letter == lists2[lists2.index(s1[0]) + r]:
#                     r += 1
#                     count += 1
#                     continue

#                 # if count + 1 == len(s1):
#                 #     return True
#                 #     break

#                 else:
#                     if count + 1 == len(s1):
#                         return True
#                     lists2.remove(s1[0])
#                     l, r, count = 1, 1, 0

#             return True

#         return False


# s1 = "ab"  # True
# s2 = "eidbaooo"

# s1 = "ab"  # False
# s2 = "eidboaoo"

# s1 = "adc"  # True
# s2 = "dcda"


# Output: false

# sol = Solution()
# print(sol.checkInclusion(s1, s2))


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_freqs = [0] * 26
        s2_freqs = [0] * 26
        left_ptr = 0

        for i in range(len(s1)):
            s1_freqs[ord(s1[i]) - ord("a")] += 1
            s2_freqs[ord(s2[i]) - ord("a")] += 1

        for i in range(len(s1), len(s2)):
            if s1_freqs == s2_freqs:
                return True
            s2_freqs[ord(s2[i]) - ord("a")] += 1
            s2_freqs[ord(s2[left_ptr]) - ord("a")] -= 1
            left_ptr += 1

        if s1_freqs == s2_freqs:
            return True
        return False


# # solution from leetcode

# class Solution:
#     def checkInclusion(self, s1: str, s2: str):
#         # cnt_1 = collections.Counter(s1)
#         cnt_1 = {}
#         for s in s1: cnt_1[s] = cnt_1.get(s, 0) + 1
#         len_s1 = len(s1)

#         for i in range(len(s2) - len_s1 + 1):
#             sub_str = s2[i: i + len_s1]
#             cnt_2 = collections.Counter(sub_str)
#             if cnt_1 == cnt_2:
#                 return True

#         return False
