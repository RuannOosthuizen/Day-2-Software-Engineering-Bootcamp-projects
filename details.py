# Here I am collecting data from the user using the input funtion with the string and integer funtion, then storing that data in variables.
user_name = str(input("Please enter your NAME here: "))
user_age = int(input("Please enter your AGE here: "))
user_house_number = int(input("Please enter your HOUSE NUMBER here: "))
user_street_name = str(input("Please enter your STREET NAME here: "))

# Here I am then taking the variables I have declrade above and printing it on one single line using the f-string funtion to combine string and integers data using the varbiales.
print(f"This is {user_name} they are {user_age} years old and live at house number {user_house_number} on {user_street_name}.")
