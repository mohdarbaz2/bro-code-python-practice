# conditional expression = A one-line shortcut for the if-else statement
# X if condition else Y

name = input("Enter your full name: ")
phone_number = input("Enter your phone #: ")

print("\n--- STRING FUNCTIONS ---")

print("Length:", len(name))
print("Find A:", name.find("A"))
print("Find last o:", name.rfind("o"))
print("Capitalized:", name.capitalize())
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Is digit:", name.isdigit())
print("Is alpha:", name.isalpha())

print("\n--- PHONE FUNCTIONS ---")

print("Dash count:", phone_number.count("-"))
print("Without dashes:", phone_number.replace("-", " "))

print("\n--- HELP FOR STRING METHODS ---")
help(str)