import turtle
from math import pi,cos,sin             
                                      
                                      
r=15                                   # y' = -xsin(t)+ycos(t)
turtle.penup()                         # x' = xcos(t)+ysin(t)
turtle.pencolor("white")
turtle.bgcolor("black")
turtle.fillcolor("red")
turtle.begin_fill()
#turtle.pencolor('black')
turtle.write("My Sweet Heart",font=40,align="center")

for angle in range(360):
    angle_radian = (pi/180)*angle
    x = r*16*pow(sin(angle_radian),3) 
    y = r*(13*cos(angle_radian)-5*cos(2*angle_radian)-2*cos(3*angle_radian)-cos(4*angle_radian)) 
    turtle.goto(x,y)
    turtle.pendown()
turtle.end_fill()  
turtle.ht()
    
turtle.mainloop() 