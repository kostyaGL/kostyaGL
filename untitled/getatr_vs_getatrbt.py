class GetAttr(object):
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):
    eggs = 88
    def __init__(self):
        self.spam = 77
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr =='__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(80, '='))
    x = Class()
    x.eggs
    x.spam
    x.other
    len(x)
    try:
        x[0]
    except:
        print('fail []')
    try:
        x + 99
    except:
        print('fail +')
    try:
        x()
    except:
        print('fail ()')
    x.__call__()
    print(x.__str__())
    print(x)

#    a = GetAttr()
#    print dir(a)
