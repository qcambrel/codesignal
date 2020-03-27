def isListPalindrome(head):
    if not head:
        return True
    current = head
    forwards = [current.value]
    while current.next:
        forwards.append(current.next.value)
        current = current.next
    current = reverse_list(head)
    backwards = [current.value]
    while current.next:
        backwards.append(current.next.value)
        current = current.next
    return forwards == backwards


def reverse_list(head):
    current = head
    next = None
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head