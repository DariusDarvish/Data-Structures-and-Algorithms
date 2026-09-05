def mergeSort(items):
    #base case
    if len(items)==1 or len(items)==0:
        return items

    #recursive case
    midpoint=len(items)//2
    left=items[:midpoint]
    right=items[midpoint:]

    left_side=mergeSort(left)
    right_side=mergeSort(right)
  
    return sort_lists(left_side,right_side)

def sort_lists(left_side,right_side):
    print(left_side,right_side)
    final_list=[]
    left=0
    right=0
    while left<len(left_side) and right<len(right_side):
        if left_side[left]<right_side[right]:
            final_list.append(left_side[left])
            left+=1
        else:
            final_list.append(right_side[right])
            right+=1

    if left<len(left_side):
        final_list=final_list+left_side[left:]
    if right<len(right_side):
        final_list=final_list+right_side[right:]
    return final_list

print(mergeSort([6,5,4,9,1,2]))
