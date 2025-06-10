"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pointer1 = 0
        pointer2 = 0
        res = []
        while pointer1 < len(nums1) and pointer2 < len(nums2):

            if nums1[pointer1] < nums2[pointer2]:
                res.append(nums1[pointer1])
                pointer1 += 1
            else:
                res.append(nums2[pointer2])
                pointer2 += 1
        res.extend(nums1[pointer1:])
        res.extend(nums2[pointer2:])
        if not len(res) % 2 == 0:
            return float(res[len(res) // 2])
        else:
            return (res[(len(res) // 2) - 1] + res[len(res) // 2]) / 2


assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.00000
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
