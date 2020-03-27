def reverseNodesInKGroups(l, k):
    if not l:
        return l
    current = l
    n = k
    while current and n:
        current = current.next
        n -= 1
    if n:
        return l

    current = l
    prev = None
    next = None
    n = k
    while current and n:
        next = current.next
        current.next = prev
        prev = current
        current = next
        n -= 1
    if next:
        l.next = reverseNodesInKGroups(next, k)
    return prev