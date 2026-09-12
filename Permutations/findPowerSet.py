visited = []
def subsets(characters, index, subset):
    if index >= len(characters):
        visited.append(subset.copy())
        return

    #Use recursion without a loop when the decision is 
    # “do this” or “don’t do this” on the next step.
    char = characters[index]

    subset.append(char)
    subsets(characters, index + 1, subset)
    subset.pop()

    subsets(characters, index + 1, subset)

    return visited


print(subsets(['A', 'B', 'C'], 0, []))

