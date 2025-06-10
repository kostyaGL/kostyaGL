from typing import List

"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""


class Solution:
    def filter_out(self, words, step, maxWidth):
        result = []
        start_point = 0
        elements_len = 0
        for ind in range(step, len(words)):
            arr = words[ind]
            if maxWidth == len(arr) and not result:
                return 0, [arr]
            if maxWidth > start_point + len(arr):
                start_point += len(arr) + (1 if len(result) else 0)
                result.append(arr)
                elements_len += len(arr)
            else:
                return maxWidth - elements_len, result
        return maxWidth - elements_len, words[step:]

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        step = 0
        ff = []
        while not step == len(words):
            ll, arr = self.filter_out(words, step, maxWidth)
            step += len(arr)
            ln = len(arr) - 1 if (len(arr)) > 1 else len(arr)
            res = [0] * ln
            for i in range(ll):
                res[i % ln] += 1
            if not step == len(words):
                for bb, reee in enumerate(res):
                    arr[bb] += ' ' * reee
                ff.append(''.join(arr))
            else:
                rr = ' '.join(arr)
                a = rr.ljust(maxWidth)
                ff.append(a)
        return ff


print(Solution().fullJustify(
    words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(Solution().fullJustify(
    words=
    ["Listen", "to", "many,", "speak", "to", "a", "few."], maxWidth=6))

print(Solution().fullJustify(
    words=
    ["What", "must", "be", "shall", "be."], maxWidth=5))

print(Solution().fullJustify(
    words=
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], maxWidth=20))
