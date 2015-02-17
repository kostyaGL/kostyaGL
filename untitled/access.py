class Q(object):
    a = 1
    def test(self):
        self.b = 1
        print "change %s" % self.b
class A(Q):
    k = 2
    def test2(self):
        self.c = 3
        print "change %s" % self.c
a = A()
a.k = 3
a.c = 4
print a.__dict__
a.test2()