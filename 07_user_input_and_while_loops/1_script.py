# 'time' module handles time-related tasks
import time

# 'int(input())' converts the user input to an integer
number_in_group = int(input("please enter the number of people in the dinner group: "))

if number_in_group >= 8:
    print(f"let me check if we have a table for {number_in_group} available...")

    # 'time.sleep()' pauses the program for a given number of seconds
    time.sleep(2)
    print("please wait for a table :)")
else:
    print("your table is ready...")

# notes
    # 'input()' defaults to a string