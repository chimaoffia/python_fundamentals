 # building a bmi calculator
weight = input("plese enter your weight in kg \n")
height = input("please enter your hieght in m \n")

bmi =int(weight) / float(height) ** 2
bmi_result = float(bmi)

if bmi_result < 18.5:
    print(f"your bmi is{bmi_result},you are underweight.see a doctor ")

elif bmi_result > 18.5 and bmi_result < 24.9:
    print(f"your bmi is {bmi_result}, you are healthy")

elif bmi_result > 25 and bmi_result < 29.9:
    print(f"your bmi is {bmi_result}, you are overweight")

elif bmi_result > 30 and bmi_result < 35:
    print(f"your bmi is {bmi_result},you are obese")
    
else:
    print(f"your bmi is {bmi_result}, see ur doctor")
