from bisect import bisect_left, bisect_right

class intervalmap(object):

    def __init__(self):

        self._bounds = []
        self._items = []
        self._upperitem = None

    def __setitem__(self,_slice,_value):

        assert isinstance(_slice,slice), 'The key must be a slice object'

        if _slice.start is None:
            start_point = -1
        else:
            start_point = bisect_left(self._bounds,_slice.start)

        if _slice.stop is None:
            end_point = -1
        else:
            end_point = bisect_left(self._bounds,_slice.stop)

        if start_point>=0:
            if start_point < len(self._bounds) and self._bounds[start_point]<_slice.start:
                start_point += 1

            if end_point>=0:
                self._bounds[start_point:end_point] = [_slice.start,_slice.stop]
                if start_point < len(self._items):
                    self._items[start_point:end_point] = [self._items[start_point],_value]
                else:
                    self._items[start_point:end_point] = [self._upperitem,_value]
            else:
                self._bounds[start_point:] = [_slice.start]
                if start_point < len(self._items):
                    self._items[start_point:] = [self._items[start_point],_value]
                else:
                    self._items[start_point:] = [self._upperitem]
                self._upperitem = _value
        else:
            if end_point>=0:
                self._bounds[:end_point] = [_slice.stop]
                self._items[:end_point] = [_value]
            else:
                self._bounds[:] = []
                self._items[:] = []
                self._upperitem = _value

    def __getitem__(self,_point):

        assert not isinstance(_point,slice), 'The key cannot be a slice object'

        index = bisect_right(self._bounds,_point)
        if index < len(self._bounds):
            return self._items[index]
        else:
            return self._upperitem


i = intervalmap()
i['14:00':'16:00'] = 'Vlad'
print i['15:00']

def ch(a,l=[]):
     l.append(a)
     return l
print ch(1)
print ch(1)



