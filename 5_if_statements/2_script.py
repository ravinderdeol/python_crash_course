alien_colour = "red"

# 'else' can be omitted in an if-elif chain
if alien_colour == "green":
    points = 5
elif alien_colour == "yellow":
    points = 10
elif alien_colour == "red":
    points = 15

print(f"you earned {points} points")

# notes
    # 'else' is a catchall statement that executes if no other conditions are met
    # 'if-elif-else' chains are good if you want one condition to pass
    # 'if statements' multiples of them are good if you need to test multiple conditions