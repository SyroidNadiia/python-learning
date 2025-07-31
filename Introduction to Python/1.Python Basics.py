# Calculations with variables
# You've now created a savings variable, so let's start saving!

# Instead of calculating with the actual values, you can use variables instead.

# How much money would you have saved four months from now, if you saved $10 each month?

# Create the variables monthly_savings and num_months
monthly_savings = 10

num_months = 4

# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months

# Print new_savings
print(new_savings)


# Other variable types
# In the previous exercise, you worked with the integer Python data type:

# int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
# Next to numerical data types, there are three other very common data types:

# float, or floating point: a number that has both an integer and fractional part, separated by a point. 1.1, is an example of a float.
# str, or string: a type to represent text. You can use single or double quotes to build a string.
# bool, or boolean: a type to represent logical values. It can only be True or False (the capitalization is important!).

# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True

# Operations with other types
# Variables come in different types in Python. You can see the type of a variable by using type(). For example, to see type of a, execute: type(a).

# Different types behave differently in Python. When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

# Time for you to test this out.

savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))