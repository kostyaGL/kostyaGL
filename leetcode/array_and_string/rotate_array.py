"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
[2, 3, 1, 7, 4, 5, 6]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def reverse(nums, start, end):
    while end >= start:
        r = nums[start]
        l = nums[end]
        nums[start] = l
        nums[end] = r
        start += 1
        end -= 1


def rotate_array(nums, k):
    ln = len(nums)
    k %= len(nums)
    reverse(nums, ln - k, ln - 1)
    reverse(nums, 0, (ln - k) - 1)
    reverse(nums, 0, ln - 1)
    print(nums)


print(rotate_array(nums=[1, 2, 3, 4, 5, 6, 7], k=3), [5, 6, 7, 1, 2, 3, 4])
print(rotate_array(nums=[1, 2, 3, 4, 5, 6], k=11))



