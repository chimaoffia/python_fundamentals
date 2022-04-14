# it means checking or etilation through a code

# types of lopes while and for lope.




i = 0
while i < 5:
    print(i)
    i += 1



#iterable
#for 

for x in "python is fun":
    print(x)


total_score = 0

final_year_result = [30, 70, 80, 90, 60]

for scores in final_year_result:
    # total_score = 0
    total_score += scores
    # print(total_score)
    
print(total_score)


students = ["chima", "mike", "chuks"]
for student in students:
    if student == "mike":
        print("your attention is needed by vc")


    
print(range(10))
for item in range(10):
    print(item)

    # break is used to end a program
    # if item == 5:
    #      break
 #continue 
    if item == 5:
         print("you passed")
         continue
    

    #nested lopes

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c"]

for number in numbers:
    print(number)
    for items in letters:
        print(items)
