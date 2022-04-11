#set is an on ordered collections of data....in a set we dont have duplicate.. and set is not and index base..


import numbers


numbers = {1,1,3,3,7,2,5}
print(numbers)  # it picks only one of the duplicated numbers and printed it in orderly manner.

#coverting list to a set
email_list =["chima@gmail.com","mike@gmail.com","chima@gmail.com"]

new_list = set(email_list)
print(new_list)
print(new_list[0])

print("vincent" in email_list)
