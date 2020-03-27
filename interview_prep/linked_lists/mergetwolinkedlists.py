def mergeTwoLinkedLists(l1, l2):
    if not l1 or (l2 and (l1.value > l2.value)):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLinkedLists(l1.next, l2)
    return l1