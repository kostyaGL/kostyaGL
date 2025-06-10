"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = []
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                l.append(i)
                magazine.remove(i)
        if len(l) == len(ransomNote):
            return True
        else:
            return False


print(Solution().canConstruct("a", 'b'))
