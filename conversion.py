# Here I am declaring the following varbiales as instructed by the task guide:
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# Here I then use the conversion method of using the int() and str() funtions to convert the variables into different data types and storing those into a new variable.
# num1 into an integer:
int_num1 = int(num1)
# num2 into a float:
float_num2 = float(num2)
# num3 into a string:
str_num3 = str(num3)
# string1 into an integer:
int_string1 = int(string1)

# Here I print out all the new varbiales with their new data types as well as printing out their data types just to confirm they were converted:
print(int_num1)
print(float_num2)
print(str_num3)
print(int_string1)

print(type(int_num1))
print(type(float_num2))
print(type(str_num3))
print(type(int_string1))