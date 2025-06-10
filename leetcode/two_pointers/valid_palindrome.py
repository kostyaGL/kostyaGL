import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        ls = len(s)
        st, st1 = 0, ls - 1
        while ls > 1:
            # print(s[st], s[st1])
            if not s[st] == s[st1]:
                return False
            st += 1
            st1 -= 1
            ls -= 2
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
