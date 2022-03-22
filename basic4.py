# logical statement

phone_ring = "mike"

if phone_ring == "mike" :
    print("pick up yhe phone")

else:
    print("drop the phone") 


# NESTED IF
student = input("are you a student ?")

if student.lower() == "yes":
    age = int(input("please enter your age\n"))
    if age < 12:
        print(f"oh you are {age} years old, please enter free")

    elif age > 12 and age < 19:
        print(f"your are {age} years old, please pay 200 naira")
    else:
        print(f"you are {age} years old, and you need to pay 1000 naira")    


else:
    print(f"sorry this program is not for you")

