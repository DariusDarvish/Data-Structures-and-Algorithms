visited=[]
def seatingCharts(seating_chart,current_chart):
    if len(current_chart)==len(seating_chart):
        visited.append(current_chart.copy())
        return

    #Use a for loop when you are iterating through options at a level.
    for x in seating_chart:
        if x not in current_chart:
            current_chart.append(x)
            seatingCharts(seating_chart,current_chart)
            #This removes the most recently added item so the recursion can try the next branch.
            current_chart.pop()

    return visited

print(seatingCharts(['Alice','Ben','Claude'],current_chart=[]))
