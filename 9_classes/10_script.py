from restaurant import Restaurant as R, IceCreamStand as ICS

# create an insance of a class
my_ice_cream = ICS("Ice Cream Hut", "American")

# using dot notation to call a method
my_ice_cream.describe_restaurant()
my_ice_cream.display_flavours()

# notes
    # you can store classes in modules and import the classes you need
    # write a docstring for each module that you create
    # each class in a module should be related somehow
    # it is best not to import all classes from a module using the asterisk
    # it is best to import a specific class or import all classes use an alias