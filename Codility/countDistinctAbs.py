def countDistinctAbsolute(A):
    setVals = set(map(lambda x:abs(x), A))
    return len(setVals)
