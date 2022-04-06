fruits = ["apple", "banana", "cherry", "apricot"]

a_fruits = []

for fruit in fruits:

    # check to see if the fruit starts with the letter 'a'
    if "a" in fruit[0]:
        a_fruits.append(fruit)

print(a_fruits)

# notes
    # 'a_fruits = [fruit for fruit in fruits if "a" in fruit[0]]' list comprehension alternative to code above
