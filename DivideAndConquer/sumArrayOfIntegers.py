def summingArray(array):
    #Base case
    if len(array)==0:
        return 0

    if len(array)==1:
        return array[0]

    split=len(array)//2

    left=array[:split]
    right=array[split:]
    left_side=summingArray(left)
    right_side=summingArray(right)
    return left_side+right_side

print(summingArray([1,2,3,4]))

