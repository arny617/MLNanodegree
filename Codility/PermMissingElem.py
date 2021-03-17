### Find missing element in Array !
def solution(A):
    # write your code in Python 3.6
    maxA = len(A)+1
    return ((maxA*(maxA+1)//2) - sum(A))
