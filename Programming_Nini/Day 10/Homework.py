#Homework 1 

i = 1

while i < 100:
    print(str(i) + " " + ("kenti"))
    i += 2

#Homework 2

age = int(input("how old are you?: "))
fathers_age = int(input("how old is your father? : "))

if fathers_age * 2 > age:
    print("Bingo!!!")
else:
    print("Mouse!!")

#Homework 3


gender_check = input("male or female? : ")
age_check = input("How old are you? : ")


if gender_check == ("male"):
    print("pensia gekutvnit")
else:
    if gender_check ==  ("female"):
        print("tqven gekutvnit pensia")

if gender_check == "non binery":
    print("gamaswari aqedan ;d")


if age_check == 65:
    print("pensia gekutvnit")

if age_check == 60:
    print("tqven gekutvnit pensia")


#Homework 4

ask_about_education = input(" are you member of GOA? : ")



if ask_about_education == "Yes":
    print("You are the mostly clever and lucky<3 you can understand how much important is education!")
else:
    print("You can't understand how much important is education couse you are nerd. join GOA!")