def getPerms(chars):
    #base case
    if len(chars)==1:
        return [chars]

    permutations=[]
    head=chars[0]
    tail=chars[1:]

    tailPermutations=getPerms(tail)
    for tailPerm in tailPermutations:
        for i in range(len(tailPerm) + 1):
            newPerm = tailPerm[0:i] + head + tailPerm[i:]
            permutations.append(newPerm)
    return permutations


print(getPerms('ABCD'))