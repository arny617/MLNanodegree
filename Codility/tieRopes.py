### K = minimum size of rope
### A = array of rope sizes
def tieRopes(K,A):
    count = 0
    ropeLength = 0
    for item in A:
        ropeLength+=item
        if ropeLength>=K:
            count+=1
            ropeLength=0
    return count
