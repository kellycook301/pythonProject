import math
# importing math so that it may be used in functions. See below.
# the "math.ceil" in the function makes it so that the number
# is being rounded up to the nearest integer. That way
# a total isn't throw with a bunch of additional numbers after the
# dollar amount

# defining function named "split_check"
def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

total_due = float(input ("What is the total?  "))
number_of_people = int(input("How many people?  "))
amount_due = split_check(total_due, number_of_people)


print("Each person owes ${}. Pay up!".format(amount_due))