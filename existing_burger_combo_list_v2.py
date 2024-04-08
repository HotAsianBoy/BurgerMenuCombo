"""Existing Burger Combo List v2
Simplify the code that allows the user to see all existing combo meals
as it will work simply as a dictionary at the start of the main program"""

# List of each combo meal and price for each, being  dictionary to store the combo meals with their details
combo_meals = {
    'Combo 1 = Value': {'items': ['Beef Burger', 'Fries', 'Fizzy Drink'], 'price': 6.69},
    'Combo 2 = Cheesy': {'items': ['Cheese Burger', 'Fries', 'Fizzy Drink'], 'price': 8.69},
    'Combo 3 = Super': {'items': ['Cheese Burger', 'Large Fries', 'Smoothie'], 'price': 10.69}
}
print(combo_meals)
