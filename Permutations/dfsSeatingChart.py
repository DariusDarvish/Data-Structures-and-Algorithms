visited=[]
def seatingCharts(seating_chart,current_chart):
    if len(current_chart)==len(seating_chart):
        visited.append(current_chart.copy())
        return
    
    for x in seating_chart:
        if x not in current_chart:
            current_chart.append(x)
            seatingCharts(seating_chart,current_chart)
            #This step is the key to set up the search by removing the charatcer we are allowing for us to create the recursion branches
            current_chart.pop()

    return visited

print(seatingCharts(['Alice','Ben','Claude'],current_chart=[]))
