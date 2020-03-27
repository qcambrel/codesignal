def addTwoHugeNumbers(a, b):
    huge_sum = str(process_numbers(a) + process_numbers(b))
    if len(huge_sum) % 4 != 0:
        huge_sum = "0" * (4 - len(huge_sum) % 4) + huge_sum
    return list(map(
        int, list(map(''.join, zip(*[iter(huge_sum)] * 4)))))


def process_numbers(num_list):
    head = num_list
    store = [head.value]
    current = head
    while current.next:
        current = current.next
        store.append(current.value)
    store = list(map(str, store))
    
    for i in range(len(store)):
        if len(store[i]) < 4:
            store[i] = "0" * (4 - len(store[i])) + store[i]

    huge_num = int("".join(store))
    return huge_num
    