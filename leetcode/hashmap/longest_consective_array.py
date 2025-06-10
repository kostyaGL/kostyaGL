from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        longest_val = 0
        for i in d:
            if i - 1 not in d:
                current_num = i
                current_val = 1

                while current_num + 1 in d:  # Check for consecutive numbers in the set
                    current_num += 1
                    current_val += 1

                longest_val = max(current_val, longest_val)  # Update the longest streak

        return longest_val
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
