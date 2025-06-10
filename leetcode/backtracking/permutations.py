"""
Given an array nums of distinct integers, return all the possible letter_perms. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


# class Solution(object):
#
#     def permute1(self, nums):
#         if len(nums) == 1:
#             yield nums
#         for i in range(len(nums)):
#             for per in self.permute1(nums[i + 1:] + nums[:i]):
#                 yield [nums[i]] + per
#
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         return [i for i in self.permute1(nums)]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        if len(nums) == 1:
            return [nums[:]]

        # Select one value and remove from nums and append to list recursively
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)  ## Add multiple array with extend
            nums.append(n)
        return res


print(Solution().permute([1, 2, 3]))
