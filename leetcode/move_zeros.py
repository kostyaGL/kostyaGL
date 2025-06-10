"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


def move_zeros(nums):
    step = 1
    last_zero = 0
    while len(nums) > step and 0 in nums:
        if nums[last_zero] == 0 and nums[step] == 0:
            step += 1
        elif nums[step] == 0:
            last_zero += 1
        elif nums[last_zero] == 0:
            res = nums[step]
            nums[step] = 0
            nums[last_zero] = res
            last_zero += 1
            step += 1
        else:
            step += 1
    return nums


print(move_zeros(nums=[0, 1, 0, 3, 12]))
print(move_zeros(nums=[1, 0, 1]))
print(move_zeros(nums=[4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
print(move_zeros(
    nums=[-14831, -40022, -16541, 38489, -29759, 50260, 46185, 80664, 0, 76743, -33918, -28070, -65802, 7215, 17397,
          16777, 17636, -38282, 0, 78759, 45613, -70943, 51497, -42007, 78849, 91519, 92444, 71217, 10087]))
