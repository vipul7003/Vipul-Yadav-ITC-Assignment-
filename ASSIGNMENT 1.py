# name = Vipul Yadav SID - 22107003
# prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# calculate the average
avg = (num1 + num2 + num3) / 3

# display the result
print("The average of", num1, ",", num2, "and", num3, "is", avg)


num1 = 25
num2 = '25'
num3 = 25.0

# Convert num2 to an integer
num2 = int(num2)

# Add the three numbers together
total = num1 + num2 + num3

# Convert the total to a string
total_str = str(total)

# Print the total as a string
print(total_str)



# get the number of seconds from the user
total_seconds = int(input("Enter a number of seconds: "))

# calculate the number of minutes and seconds
minutes = total_seconds // 60
seconds = total_seconds % 60

# print the result
print(total_seconds, "seconds is equal to", minutes, "minutes and", seconds, "seconds")



# get the user's gross income and number of dependents
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents you have: "))

# calculate the taxable income
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_dependents)

# calculate the tax
tax_rate = 0.20
tax = taxable_income * tax_rate

# display the result
print("Your taxable income is:", taxable_income)
print("Your tax is:", tax)


import math

# loop over angles in 15 degree increments
for angle in range(0, 346, 15):
    # convert angle to radians
    radians = math.radians(angle)
    
    # calculate sine and cosine
    sine = round(math.sin(radians), 4)
    cosine = round(math.cos(radians), 4)
    
    # print result
    print(f"Angle: {angle} degrees")
    print(f"Sine: {sine}")
    print(f"Cosine: {cosine}")
    print()
