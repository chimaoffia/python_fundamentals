number_of_years_to_live = 90
age = input("please enter your age: ")

number_of_days_in_a_year = 365
number_of_weeks_in_a_year = 52
number_of_months_in_a_year = 12
years_remaining = number_of_years_to_live - int(age)
months_remaining = years_remaining * number_of_months_in_a_year
weeks_remaining = years_remaining * number_of_weeks_in_a_year
days_remaining = years_remaining * number_of_days_in_a_year

print(f"you have {years_remaining} years or {months_remaining} months or {weeks_remaining} weeks or {days_remaining} days remaining to live ")