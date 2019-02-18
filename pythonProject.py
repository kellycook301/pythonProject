# if statement in python
first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Kelly":
    print(first_name, "is learning Python")
print("Have a great day, {}!".format(first_name))

dessert = "chocolate" + " marshmallows"
quote = "A person who never made a mistake never tried anything new"
newQuote = "A PERSON WHO NEVER MADE A MISTAKE NEVER TRIED ANYTHING NEW"
subject_template = "Thanks for learning {} with us, {}!"
subject_template.format("Javascript", "Kelly")
print("You just bought {} {} from us, {}.".format(3, "fidget cubes", "Kelly"))

print(quote.upper())
print(newQuote.lower())

print(dessert)

# establishing that "fruit" equals "apples"
fruit = "apples"
# checking to see if "fruit" equals "apples"
fruit == "apples"
# checking to see if "fruit" equals
fruit == "oranges"