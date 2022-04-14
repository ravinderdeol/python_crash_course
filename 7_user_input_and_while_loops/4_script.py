# 'time' module handles time-related tasks
import time

ordered_pizzas = ["buffalo", "pepperoni", "hawaiian", "vegetarian", "vegetarian"]

finished_pizzas = []

print("haiwaiian - unavaiable \n")

# 'while' loop to check if 'haiwaiian' is in 'ordered pizzas' and it will run if so
while "hawaiian" in ordered_pizzas:
    ordered_pizzas.remove("hawaiian")

# 'while' loop equates to true if there are items in 'ordered pizzas'
while ordered_pizzas:

    # '.pop()' method removes the last item in 'ordered pizzas' list first
    current_pizza = ordered_pizzas.pop()

    print(f"{current_pizza} - in progress")

    # '.append()' method adds the current pizza to the 'finished pizzas' list
    finished_pizzas.append(current_pizza)

    # 'time.sleep()' method delays the program for one second
    time.sleep(1)

print("\ntypes of pizzas made:")

# 'set()' lists the different types of pizzas made
for pizza in set(finished_pizzas):
    print(f"- {pizza}")

# notes
    # use a 'while' loop to modify a list as you work through it not a 'for' loop