# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/10/2024
# Description: Calculates the number of coins required for a given amount in cents.
print("Please enter an amount in cents less than a dollar.")
amount = int(input())
print("Your change will be:")
quarters = amount // 25
amount = amount % 25
dimes = amount // 10
amount = amount % 10
nickels = amount // 5
amount = amount % 5
pennies = amount
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)