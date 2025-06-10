"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Create a hash set to keep track of characters in the current substring
        char_set = set()

        # Initialize pointers and max length variables
        left = 0
        right = 0
        max_length = 0

        while right < n:
            if s[right] not in char_set:
                # If the character is not in the set, add it to the set and expand the window
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                # If the character is already in the set, remove the character from the set and shrink the window
                char_set.remove(s[left])
                left += 1

        return max_length


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len, res = 0, 0, {}
        for right in range(len(s)):
            if s[right] not in res or res[s[right]] < left:
                res[s[right]] = right
                max_len = max(max_len, (right - left) + 1)
            else:
                left = res[s[right]] + 1
                res[s[right]] = right
        return max_len


print(Solution().lengthOfLongestSubstring("aaaabcdf"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len, res = 0, 0, {}
        for right in range(len(s)):
            if s[right] not in res or res[s[right]] < left:
                res[s[right]] = right
                max_len = max(max_len, (right - left) + 1)
            else:
                left = res[s[right]] + 1
                res[s[right]] = right
        return max_len


print(Solution().lengthOfLongestSubstring("abcef"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwked"))
print(Solution().lengthOfLongestSubstring("tmmzuxt"))

"""
aaaabcde

l = 3, r=6, mx_len=3, queque = {'a': 3, 'b': 4, 'c': 5, 'd': 6}

"""
