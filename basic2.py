


rating = 4.2
temprature = 4.0
age = 30
is_married = True
name = "chima"




print(type(rating))
print(type(age))
print(type(name))
print(type(is_married))


# type convertion  
# (convertion float to int and vis vasa)
print(int(rating))

# converting int to string 
print(type(str(age)))

# concantination joins two strings together
print("chima" + "offia")

# str and str cant concatinate so i coverted the int 33 to str.
print("chima age is" + str(33))

# formatted string  {f}
first_name = "chima"
last_name = "offia"
print(f"my name is {first_name} and my surname is {last_name} and my age is {age}")

#arithmetic operators
# print(5 + 2)  addition
# print(5 - 2)  division
# print(5 * 2)   multiplication
# print(5 % 2)   modulus
# print(5 ** 2)  esponential

# building a bmi calculator
weight = input("plese enter your weight in kg \n")
height = input("please enter your hieght in m \n")

bmi =int(weight) / float(height) ** 2
bmi_result = int(bmi)
print(bmi_result)

