a = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  21213"
b = [(71, 75), (79, 84)]
YELLOW = '\033[93m'
for k, v in b:
    a = a.replace(a[k:v], "^" * (v - k))
print "".join([c if c == "^" else " " for c in a])
