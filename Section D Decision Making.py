#Objective: Applying conditional logic.

#Positive or negative
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.\n")
elif number < 0:
    print("The number is negative.\n")
else:
    print("The number is zero.\n")

# Even or Odd
check_num = int(input("Enter a number: "))
if check_num % 2 == 0:
    print("The number is Even.\n")
else:
    print("The number is Odd.\n")

# Weather Categorization
weather_temp = float(input("Enter temperature: "))
if weather_temp > 30:
    print("Hot Weather")
else:
    print("Normal Weather")