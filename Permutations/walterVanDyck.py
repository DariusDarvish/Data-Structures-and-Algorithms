visited=[]

def walterVanDyck(balance,current,openRem,closeRem):
    if openRem==balance and closeRem==balance:
        if current not in visited:
            visited.append(current)
        return
     #Use recursion without a loop when the decision is 
     # “do this” or “don’t do this” on the next step.
    if openRem<balance:
        current=current+'('
        openRem+=1
        walterVanDyck(balance,current,openRem,closeRem)
    
    if closeRem<openRem:
        current=current+')'
        closeRem+=1
        walterVanDyck(balance,current,openRem,closeRem)

    
    return visited

print(walterVanDyck(3,'',0,0))

