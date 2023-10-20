import turtle

def snowflake(allu, lengthSide, levels): 
    if levels == 0: 
        allu.forward(lengthSide)  # Draw a straight line
        return
    lengthSide /= 3.0
    snowflake(allu, lengthSide, levels-1)  # Recursive call for 1st segment
    allu.left(60)  # Turn left by 60 degrees
    snowflake(allu, lengthSide, levels-1)  # Recursive call for 2nd segment
    allu.right(120)  # Turn right by 120 degrees
    snowflake(allu, lengthSide, levels-1)  # Recursive call for 3rd segment
    allu.left(60)  # Turn left by 60 degrees
    snowflake(allu, lengthSide, levels-1)  # Recursive call for 4th segment

# Create a turtle named "allu"
allu = turtle.Turtle()

turtle.bgcolor("black")
allu.pencolor('aqua')
allu.pensize(3)

allu.speed(0)  # Set turtle's drawing speed
length = 300.0

allu.penup()
allu.fd(-150)
allu.pendown()

# Draw 3 snowflakes
for i in range(3):     
    snowflake(allu, length, 4) 
    allu.right(120) 

turtle.done()
