numbers = []

# 'range(1, 1001)' returns numbers from 1 to 1000
for number in range(1, 1001):

    # '.append()' add each number to the numbers list
    numbers.append(number)

# 'min()' returns the smallest number in the list
# 'max()' returns the largest number in the list
print(min(numbers))
print(max(numbers))


# notes
    # 'range(1001)' would return numbers from 0 to 1000
    # 'list(range(1001))' would return a list of numbers from 0 to 1000
    # 'range(2, 11, 2)' would return numbers from 2 to 10 in steps of 2
    # 'sum()' would return the sum of all numbers in a list