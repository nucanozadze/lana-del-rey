from turtle import *

#we want to paint a house

#step 1: draw a square

width (7)

color("green")


forward (200)
left (90)


forward (200)
left (90)


forward (200)
left (90)


forward (200)
left (90)

#end of square

#drawin a door

forward (70)
color ("purple")
begin_fill()
left (90)
forward (120)    #height of the door
right (90)
forward (60)
right (90)
forward (120)
end_fill()

penup()

goto(200,200)
pendown()


color("orange")
begin_fill()
right(150)
forward (200)
left (120)
forward (200)
end_fill()

color("skyblue")
begin_fill()
left(40)
penup()
goto(120,150)
pendown()

left(260)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()    


exitonclick()