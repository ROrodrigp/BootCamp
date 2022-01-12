# Create a Python list to store your grocery list
grocery = ['Milk', 'Bread', 'Eggs', 'Peanut Butter', 'Jelly']
# Print the grocery list
print(grocery)
# Change "Peanut Butter" to "Almond Butter" and print out the updated list
grocery[grocery.index('Peanut Butter')] = 'Almond Butter'
print(grocery)
# Remove "Jelly" from grocery list and print out the updated list
grocery.remove('Jelly')
print(grocery)
# Add "Coffee" to grocery list and print the updated list
grocery.append('Coffee')
print(grocery)