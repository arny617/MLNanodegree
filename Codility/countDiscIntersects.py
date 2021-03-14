class DiscLog():
    def __init__(self,x,start_end):
        self.x=x
        self.start_end = start_end
def numDiscIntersections(A):
    discHistory = []
    for i in range(len(A)):
        discHistory.append(DiscLog(i-A[i],1))
        discHistory.append(DiscLog(i+A[i],-1))
    discHistory.sort(key = lambda d:(d.x,-d.start_end))
    intersects = 0
    active_intersects = 0
    for log in discHistory:
        active_intersects += log.start_end
        if log.start_end>0:
            intersects += active_intersects - 1
        if intersects>10000000:
            return -1
    return intersects
