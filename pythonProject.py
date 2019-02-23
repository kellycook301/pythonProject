# 1. If/Else/Elif Statements In Python
# ______________________
first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Kelly":
    print(first_name, "is learning Python")
elif first_name =="Maximiliane":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    # coercing what is returned into an integer. 
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow! You're {}! If you're confident with reading...".format(age))

    print("You should TOTALLY learn Python, {}!".format(first_name))
print("Have a great day, {}!".format(first_name))

#2. Establishing Variables
# ______________________
# dessert = "chocolate" + " marshmallows"
# quote = "A person who never made a mistake never tried anything new"
# newQuote = "A PERSON WHO NEVER MADE A MISTAKE NEVER TRIED ANYTHING NEW"
# subject_template = "Thanks for learning {} with us, {}!"
# subject_template.format("Javascript", "Kelly")
# print("You just bought {} {} from us, {}.".format(3, "fidget cubes", "Kelly"))

# print(quote.upper())
# print(newQuote.lower())

# print(dessert)

# establishing that "fruit" equals "apples"
fruit = "apples"
# checking to see if "fruit" equals "apples"
fruit == "apples"
# checking to see if "fruit" equals
fruit == "oranges"

