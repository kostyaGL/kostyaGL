# import re
#
# # a = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 21213"
# # b = [(71, 75), (79, 84)]
# #
# # YELLOW = '\033[93m'
# # END = '\033[0m'
# #
# # pat = "\d+"
# #
# # first = b[0]
# # f_ind, s_ind = first
# # rest = b[1:]
# # word = list(YELLOW + a[f_ind:s_ind] + END)
# # a = list(a)
# # a[f_ind:s_ind] = word
# # a = "".join(a)
# # if rest:
# #     for k, v in rest:
# #         ln = len(word) - len(first)
# #         word = list(YELLOW + a[k+ln:v+ln] + END)
# #         a = list(a)
# #         a[k + ln:v + ln] = word
# #         a = "".join(a)
# #         print a
# #
# import re
# colourFormat = '\033[{0}m'
# colourStr = colourFormat.format(32)
# resetStr = colourFormat.format(0)
# s = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 21213"
#
# lastMatch = 0
# formattedText = ''
# for match in re.finditer(r'\d+', s):
#     start, end = match.span()
#     formattedText += s[lastMatch: start]
#     formattedText += colourStr
#     formattedText += s[start: end]
#     formattedText += resetStr
#     lastMatch = end
# formattedText += s[lastMatch:]
#
# print formattedText