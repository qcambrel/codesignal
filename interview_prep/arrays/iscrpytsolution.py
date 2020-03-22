def isCryptSolution(crypt, solution):
    decoder = {k:v for k,v in solution}
    messages = []
    for word in crypt:
        message = "".join((map(str, [decoder[letter] for letter in word])))
        if len(message) > 1 and message[0] == '0':
            return False
        messages.append(int(message))
    return sum(messages[:-1]) == messages[-1]