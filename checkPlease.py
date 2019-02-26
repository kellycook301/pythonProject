import math
# importing math so that it may be used in functions. See below.
# the "math.ceil" in the function makes it so that the number
# is being rounded up to the nearest integer. That way
# a total isn't throw with a bunch of additional numbers after the
# dollar amount

# defining function named "split_check"
def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than one person is required to split a check")
    return math.ceil(total / number_of_people)

# might throw a SyntaxError
try: 
    total_due = float(input ("What is the total?  "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except SyntaxError:
    print("Oh no! That's not a valid value. Try again...")
except ValueError as err:
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}. Pay up!".format(amount_due))

# creating a function for something that calculates the square of
# a number passed in

def square(number):
    return(number * number)

result = square(3)
print(result)