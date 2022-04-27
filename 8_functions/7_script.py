# '**car_info' collects an arbitrary number of arguments
def add_car(manufacturer, model, **car_info):

    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = add_car("tesla", "model s", color = "black", doors = 5)

print(car)

# notes
    # '**car_info' creates an empty dictionary and packs in the values
    # you will often see '**kwargs' to collect arbitrary keyword arguments