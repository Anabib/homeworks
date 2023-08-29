from turtle import *

#we want to paint a house

speed(10)

width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window1
left(30)
penup()
goto(0, 150)
pendown()
color("blue")
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#window2
penup()
goto(200, 150)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()






exitonclick()
