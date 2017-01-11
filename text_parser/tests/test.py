import re

a = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  21213"
b = [(71, 75), (79, 84)]

YELLOW = '\033[93m'
END = '\033[0m'

pat = "\d+"

i = 0

for k, v in b:
    a = "".join(a)
    w1 = len(a[k:v])
    print w1
    word = list(YELLOW + a[k:v] + END)
    w2 = len(word)
    print w2
    i = w2 - w1
    print "".join(list(YELLOW + a[k + i:v + i] + END))

    a = list(a)
    a[k:v] = word
print "".join(a)
