active_users = ["james", "mary", "robert", "sarah", "david", "karen"]

banned_users = ["mary", "robert"]

deleted_users = ["david", "karen"]

for user in active_users:

    # 'not in' operator checks if a user is not in a list
    if user not in banned_users and user not in deleted_users:
        print(f"{user.title()} (Active)")
    else:
        print(f"{user.title()} (Remove)")

# notes
    # it can be more efficient to check for 'inequality (!=)' than 'equality (==)'
    # 'if (age_1 >= 18) and (age_2 >= 18)' parantheses improve readability ('or' operator is the opposite)
    # 'in' operator checks if a value is in a list ('not in' operator is the opposite)
    # 'True' and 'False' are boolean values used to check conditions
