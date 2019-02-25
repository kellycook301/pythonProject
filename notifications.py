# 1. Functions

# "def" for "define"
def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

# calling the "yell" method
yell("You are doing great")
yell("Don't repear yourself. Keep your code DRY")
yell("Don't forget to ask for help")

# creating dashes for the length of the word entered in

def display_blanks ( word):
    blanks = "-" * len(word)
    print(blanks)

print("Puzzle 1:")
display_blanks("treehouse")