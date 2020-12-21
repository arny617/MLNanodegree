## Insert, Delete O(1), Search O(n)
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
class L:
    def __init__(self):
        self.root = None
    def search_list(L,key):
        while L and L.data!=key:
            L = L.next
        return L
    def AtBeginning(self,newdata):
        NewNode = ListNode(newdata)
        # Update the new nodes next val to existing node
        NewNode.next = self.root
        self.root = NewNode
    def AtEnd(self, newdata):
        NewNode = ListNode(newdata)
        if self.root is None:
            self.root = NewNode
            return
        laste = self.root
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
    def insertNodeAtPosition(self,data, position):
        if self.root is None:
            return ListNode(data)
        cur = self.root
        for _ in range(position - 1):
            cur = cur.next
        cur.next, cur.next.next = ListNode(data), cur.next
        return self.root
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = ListNode(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode
    def RemoveNode(self, Removekey):
        HeadVal = self.root
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.root = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None
    # Print the linked list
    def listprint(self):
        printval = self.root
        while printval is not None:
            print (printval.data)
            printval = printval.next
