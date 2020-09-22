# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

#food = budget.Category("Food")
#food.deposit(900, "deposit")
#food.withdraw(105.55, "")
#entertainment = budget.Category("Entertainment")
#entertainment.deposit(900, "deposit")
#entertainment.withdraw(33.40, "")
#business = budget.Category("Business")
#business.deposit(900, "deposit")
#business.withdraw(10.99, "")

#print(repr(create_spend_chart([ business, food, entertainment])))

# Run unit tests automatically
main(module='test_module', exit=False)