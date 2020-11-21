### Ice Cream Parlor
def whatFlavors(cost, money):
    myDict = {}
    for i in range(len(cost)):
        compliment = money-cost[i]
        if(compliment in myDict):
            print(str(myDict[compliment]+1) + ' ' + str(i+1))
            return
        else:
            myDict[cost[i]] = i 
