def sortedInsert(head, data):
    node = DoublyLinkedListNode(data) 
    
    if head is None:
        return node 
    
    if data <= head. data:
        node.next = head
        head.prev = node 
        return node 
    else:
        remaining = sortedInsert(head.next, data) 
        head.next = remaining 
        remaining.prev = head 
        return head
