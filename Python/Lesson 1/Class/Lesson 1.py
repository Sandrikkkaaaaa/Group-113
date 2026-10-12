from turtle import *

#Making a House

#Base
width(3)

begin_fill()
color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

#Window

forward(200)
left(90)


forward(100)
color("black")
begin_fill()
left(90)

forward(25)
right(90)

forward(25)
right(90)
forward(25)
left(90)
end_fill()
color("blue")
forward(75)

left(90)
forward(200)
left(90)
forward(75)
left(90)
color("black")
begin_fill()
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()
color("blue")

left(90)
forward(100)
left(90)



#Door

forward(90)
color("green")
begin_fill()
left(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
end_fill()

color("Blue")

#Roof


left(90)
forward(90)
left(90)
forward(200)
left(45)
color("purple")
begin_fill()
forward(141.42)
left(90)
forward(141.42)
end_fill()

exitonclick()