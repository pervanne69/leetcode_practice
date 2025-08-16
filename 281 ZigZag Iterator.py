class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.index1 = 0
        self.index2 = 0
        self.turn_v1 = True

    """
    @return: An integer
    """

    def _next(self):
        if self.turn_v1 and self.index1 < len(self.v1):
            self.turn_v1 = False
            self.index1 += 1
            return self.v1[self.index1 - 1]
        elif not self.turn_v1 and self.index2 < len(self.v2):
            self.turn_v1 = True
            self.index2 += 1
            return self.v2[self.index2 - 1]
        # Если один из векторов закончился, берём из другого
        elif self.index1 < len(self.v1):
            self.index1 += 1
            return self.v1[self.index1 - 1]
        else:
            self.index2 += 1
            return self.v2[self.index2 - 1]


    """
    @return: True if has next
    """

    def hasNext(self):
        return self.index1 < len(self.v1) or self.index2 < len(self.v2)


zziter = ZigzagIterator(v1=[1, 2], v2=[])
result = []
while zziter.hasNext():
    result.append(zziter._next())
print(result)