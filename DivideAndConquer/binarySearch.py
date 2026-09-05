def binarySearch(target,shelf,left=None,right=None):
    if left is None:
        left=0
        
    if right is None:
        right=len(shelf)-1
    # Base case
    if left>right:
        return False

    midpoint=(left+right)//2
    
    # Base case
    if shelf[midpoint]==target:
        return True

    elif shelf[midpoint]>target:
        return binarySearch(target,shelf,left,right-1)

    elif shelf[midpoint]<target:
        return binarySearch(target,shelf,left+1,right)


print(binarySearch(3,[1,2,3,4,5,6,7,8,9]))
    

    
    