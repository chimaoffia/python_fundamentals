#  day 4

print("welcome to tip calculator")

total_bill = int(input("what is the total bill \n"))
tips_percentage = int(input("what percentage tip do you want to tip? 10, 12 or 15  \n"))
people = int(input("how many to split the bill \n"))
percentage = 100

tips_amount = total_bill * tips_percentage / percentage

# note the result will be the tip percentage

total_amount = total_bill + tips_amount
split_amount = total_amount/people

print(f"each of you will pay {split_amount} naira \n")