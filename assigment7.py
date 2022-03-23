  # create an authomated embassy chat. be creative and have fun with it


print("welcome to canadian embassy")

#visa types

leisure = "vacation"
school = "studies"
biz = "business"


current_year = 2022
first_name = input("please enter your first name \n")
last_name = input("please enter your last name\n")
year_of_birth = int(input("please enter year of birth\n"))

my_age = current_year - year_of_birth

print(f"welcome {last_name} {first_name}")

print(f"your are {my_age} years old.")

Purpose_of_travel = input("please what is the purpose of your travel\n")

if Purpose_of_travel == "leisure":
    print(f"you chose {leisure}")

elif Purpose_of_travel == "school":
    print(f"you chose {school}")

elif Purpose_of_travel == "biz":
    print(f"you chose {biz} ")

else:
    (" sorry we don,t offer the visa for now.thank you ")

duration_of_stay = int(input("how long will you stay in canada if approved?\n"))

if duration_of_stay <= 30 and Purpose_of_travel == "leisure":
    print(f" congratulations you have been granted a {duration_of_stay} days visa for {leisure} visa.")

elif duration_of_stay <= 4 and Purpose_of_travel == "school":
    print(f"congratulations, you have been granted a {school} visa for {duration_of_stay} years")

elif duration_of_stay <= 30 and Purpose_of_travel == "biz":
    print(f"congratulations,you have been granted a {biz} visa for {duration_of_stay} days")

else:
    print(" sorry, you have been denied the visa. thank you.")
