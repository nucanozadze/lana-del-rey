#შექმენით ფუნქცია რომელსაც გადაეცემა კვადრატის გვერდი და დაპრინტავს მის ფართობს და პერიმეტრს;
#ასევე შექმენით ფუნქცია რომელსაც გადაეცემა სამკუთხედის სამი გვერდი და დაპრინტავს მის ფართობს და პერიმეტრს;

#დავალება 1
from turtle import *
#step 1:  draw a square
speed(100)
def კვადრატის_დახაზვა():
    for i in range(4):
        forward(200)
        left(90)
კვადრატის_დახაზვა()
#end of square
#drawing a door()
forward(70)
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
#end of door
#draw a triangle
penup()
goto(200, 200)
pendown()

right(150)
forward(200)
left(120)
forward(200)
#end of triangle
#start a 1 windows
penup()
goto(15, 170)
pendown()
left(30)
forward(50)
def window():
    for i in range(3):
        left(90)
        forward(50)
window()
#end of first window
#start second window
penup()
goto(180, 170)
pendown()
def window_2():
    for i in range(5):
        forward(50)
        left(90)
window_2()
#end of house
exitonclick()


#დავალება 2


def square_properties(გვერდის_სიგრძე):
    print("ფართობი:", გვერდის_სიგრძე * გვერდის_სიგრძე)
    print("პერიმეტრი:", 4 * გვერდის_სიგრძე)


side = float(input("ჩაწერე კვადრატის გვერდის სიგრძე: "))
square_properties(side)


#დავალება 3


def triangle_perimeter(გვერდი_1, გვერდი_2, გვერდი_3):
    perimeter = გვერდი_1 + გვერდი_2 + გვერდი_3
    print("Triangle Perimeter:", perimeter)

# Example usage
გვერდი_1 = float(input("Enter the length of the first side: "))
გვერდი_2= float(input("Enter the length of the second side: "))
გვერდი_3 = float(input("Enter the length of the third side: "))
triangle_perimeter(გვერდი_1, გვერდი_2, გვერდი_3)