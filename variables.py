# the variable my_string is assigned the string "Hallo there! General Kenobi" due to the presence of the quotation marks making Python read it as a string.
my_string = "Hallo there! General Kenobi"

# the variable my_char is also included in the string data type due to the quotation marks, however it only consists of one character instead of a combination of characters.
my_char = "A"

# the variable my_integer is assigned a integer or a whole number 25, due to the lack of quotation marks making Python read it as a integer.
my_integer = 25

# the variable my_float is assaigned the first three numbesr of pie, which is a decimanl number making it a float number due to the precence of a decimal point. Making Python read it as a float.
my_float = 3.14

# the varibale my_boolean is assigned a value my the user, if this value is not the word "True" then it will have the value of False. Thus making Python read this string of code as a boolean. due to this answer being a string i have make the input a string data type by putting the input funtion int a string funtion.
# psuedocode:
# step 1: Ask the user for an input.
# step 2: Store the input data in a varbiale called "my_boolean".
# step 3: Next create a condition in an if statement. to determine the value of the variable my_boolean is true or false
# step 4: print out the corrosponding messages for the answers the user inputted.
print("Star Wars are the greatest sci fi movies ever made. True or False?")
my_boolean = str(input("Please type in your answer here: "))
if my_boolean == str("true"):
    print("That is correct!")
if my_boolean == str("True"):
    print("That is correct!")
else:
    print("You are wrong and Star Wars is awesome!")
# Here I am using the print funtion to print out the variables I have declared above, each one on a seperate line.
print(my_string)
print(my_char)
print(my_integer)
print(my_float)