"""Existing Burger Combo List v2
Simplify the code that allows the user to see all existing combo meals
as it will work simply as a dictionary at the start of the main program"""

# List of each combo meal and price for each, being a dictionary to store the combo meals with their details
combo_menu = {
    'Value': {'Items': {'Beef Burger', 'Fries', 'Fizzy Drink'}, 'Price': 6.69},
    'Cheesy': {'Items': {'Cheese Burger', 'Fries', 'Fizzy Drink'}, 'Price': 8.69},
    'Super': {'Items': {'Cheese Burger', 'Large Fries', 'Smoothie'}, 'Price': 10.69}
}
print(combo_menu)
