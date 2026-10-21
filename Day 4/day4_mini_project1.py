# Project 1: Grocery List Manager
"""
**Project 1: Grocery List Manager**

Objective:
Create a simple grocery list manager where users can add items, view the list, and remove duplicates (using set functionality).

Steps:
Ask the user to input grocery items (comma-separated).  
Store these items in a list.  
Convert the list to a set to remove duplicates.  
Display the updated grocery list.  
"""

user = str(input("Write your items in list :"))
user_list = [item.strip() for item in user.split(",")]
user_set = set(user_list)
user_list = list(user_set)
print(f"There is your final list - {user_list}")
