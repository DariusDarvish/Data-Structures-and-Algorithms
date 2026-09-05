def quickSort(items):
    #Base case
    if len(items)==1 or len(items)==0:
        return items

    left=[]
    right=[]

    pivot=items[-1]
    for x in items[:-1]:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    left_side=quickSort(left)
    right_side=quickSort(right)
    return left_side + [pivot] +right_side  

print(quickSort([2,3,1]))
