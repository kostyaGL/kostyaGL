"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""


class Solution(object):
    def trap(self, height):
        if len(height) <= 2: return 0
        left, right = 1, len(height) - 1
        lmax, rmax = height[0], height[-1]
        res = 0
        while right >= left:
            if height[left] > lmax:
                lmax = height[left]
            if height[right] > rmax:
                rmax = height[right]

            if lmax <= rmax:
                res += lmax - height[left]
                left += 1
            else:
                res += rmax - height[right]
                right -= 1
        return res


print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
