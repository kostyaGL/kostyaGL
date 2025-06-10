"""
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w_l, w_l1 = len(word1), len(word2)
        start = 0
        res = []
        while start < max(w_l, w_l1):
            if w_l > start:
                res.append(word1[start])
            if w_l1 > start:
                res.append(word2[start])
            start += 1
        return ''.join(res)
print(Solution().mergeAlternately("abcd", "pq") == "apbqcd")