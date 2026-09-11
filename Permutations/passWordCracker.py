visited = []

def passWordCracker(current_password, characters, total):
    if len(current_password) == total:
        visited.append(current_password)
        return

    for x in characters:
        passWordCracker(
            current_password + str(x),
            characters,
            total
        )
        #No undo step here since the string is immutable type

    return visited

print(passWordCracker('', ['J', 'K', 1, 2, 3], 4))