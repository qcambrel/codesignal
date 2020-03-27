def removeKFromList(head, k):
    if not head:
        return head
    
    if head.value == k:
        if head.next:
            head = head.next
        else:
            return None

    node = head
    while node and node.next:
        if node.next.value == k:
            node.next = node.next.next
        else:
            node = node.next

    if node.value == k:
        head = head.next

    return head