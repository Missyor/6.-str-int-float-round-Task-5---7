# ##code to calculate year you were born
# year = input("Enter the current year: ")
# age = input("What age will you be at the end of the year?: ")
# print("You were born in", year - age)

# ##error occurs - can't subtract two strings
# print("\n")
# ###How can we fix the problem
# ##Use int - changes strings to numerical
# year = int(input("Enter the current year: "))
# age = int(input("What age will you be at the end of the year?: "))
# print("You were born in", year - age)
# print("\n")

# ###programe to convert celcius to fahrenheit
# centigrade = float(input("Enter centigrade value: "))
# fahrenheit = 9/5 + centigrade*32
# print(centigrade, "degrees celcius equals ", fahrenheit, "degrees Fahrenheit")

# ###How can we get rid of all of the decimal places.
# ###We use the ROUND function. The function goes around the variable you want to round. Here I'll round to 1 decimal place

# centigrade = float(input("Enter centigrade value: "))
# fahrenheit = 9/5 * centigrade + 32
# print(centigrade, "degrees celcius equals", round(fahrenheit, 1), "degrees Fahrenheit")

# ##How would you amend this code to round to 3 decimal places. Try the input 21.67
# centigrade = float(input("Enter centigrade value: "))
# fahrenheit = 9/5 * centigrade + 32
# print(centigrade, "degrees celcius equals", round(fahrenheit, 3), "degrees Fahrenheit")

# ###Does the table help to verify the code?
# ##Type a string in to your code instead of a number, what happens?
# ###What does the command FLOAT do?
