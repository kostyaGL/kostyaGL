traceMe = False
def trace(*args):
    if traceMe: print('[' + "".join(map(str, args)) + "]")
def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))
def public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

if __name__ == '__main__':
    traceMe = True
    @private('data', 'size', 'display')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])
    print(X.label)
    X._onInstance__wrapped.display(); X.double();
    print(Y.label)
#    Y.display(); Y.double()
#    Y.label = 'Spam'
#    Y._onInstance__wrapped.display()