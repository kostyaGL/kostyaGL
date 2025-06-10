"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.


Manacher's algorithm
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join(f'^{s}$')
        n = len(t)
        P = [0] * n
        C, R = 0, 0
        for i in range(1, n - 1):
            P[i] = int((R > i) and min(R - i, P[2 * C - i]))
            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        max_len = max(P)
        center_idx = P.index(max_len)
        return s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]


print(Solution().longestPalindrome('babad'))
# assert Solution().longestPalindrome('asfafsafsasfasfasxasd') == 'afsafsasfasfa', Solution().longestPalindrome('asfafsafsasfasfasxasd')
# assert Solution().longestPalindrome('cbbd') == 'bb'
print(Solution().longestPalindrome('dsabadda'))
