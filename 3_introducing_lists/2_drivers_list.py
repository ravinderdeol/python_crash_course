redbull = []

# 'append' adds an element to the end of the list
redbull.append("verstappen")
redbull.append("perez")

redbull_champion = "verstappen"

# 'remove' removes the first occurance from a list unless a loop is used
redbull.remove(redbull_champion)

print(f"{redbull_champion} is the redbull champion")

# notes
    # 'redbull.insert(0, "perez")' would insert perez at index zero
    # 'del drivers[0]' would delete the first list element and it would be unuseable
    # 'drivers.pop()' would delete the last list element or from a position and it would be useable