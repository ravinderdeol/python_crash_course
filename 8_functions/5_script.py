# 'order' function gets direct access to list passed into it§
def order(ordered_pizzas):
    
    # the while loop will run as long as there is an item in the list
    while ordered_pizzas:
        order = ordered_pizzas.pop()
        print(f"Order: {order.title()}")
        completed_pizzas.append(order)

def show_completed_pizzas(completed_pizzas):

    print("\nCompleted Pizzas:")
    
    for pizza in completed_pizzas:
        print(f"{pizza.title()}")

ordered_pizzas = ["pepperoni", "vegetarian", "margherita"]
completed_pizzas = []

order(ordered_pizzas[:])
show_completed_pizzas(completed_pizzas)

# notes
    # changes made to a list in a function are permanent unless you use a slice notation
    # 'order(ordered_pizzas[:])' is an example of a slice notation
    # each function should do one job
    # you can call a function from another function