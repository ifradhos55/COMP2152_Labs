# Sample Coding Questions 01 Week 01
# Ifrad Hossain

# Defining Variables
arr = [1, 4, 7, 9]

# Order of Operations
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
print(e)

# Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Common Functions
userAge = int(input("Enter your age: "))
userAge += 22
print("Now showing the shop items filtered by age: {}".format(userAge))
