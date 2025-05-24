print("Welcome to New West Fruit Store's Cost Calculator!\n")

print("Here's the list of our fruit prices:\nOranges = $3.56 per kg\nApples = $3.80 per kg\nBananas = $1.72 per kg\n\n")

print("How many kilograms are you buying for each fruit?")
oranges = float(input("Oranges-> "))
apples = float(input("Apples-> "))
bananas = float(input("Bananas-> "))

total = 3.56 * oranges + 3.80 * apples + 1.72 * bananas
print("\nYou have $" + str(total) + " Worth of fruits")
print("Thank you for a shopping here in New West Fruit Store!")