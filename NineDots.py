import turtle

# Create a Turtle object
t = turtle.Turtle()

turtle.bgcolor("black")
t.pencolor('aqua')
t.pensize(3)


# Set the distance between pairs of grids
pair_distance = 100
dot_distance=30

# Set the number of rows and columns for each grid
num_rows = 3
num_columns = 3

# Function to draw a 3x3 grid of dots
def draw_grid(x, y):
    for row in range(num_rows):
        for column in range(num_columns):
            dot_x = x + column * dot_distance
            dot_y = y - row * dot_distance
            draw_dot(dot_x, dot_y)

# Function to draw a dot at the given position
def draw_dot(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(10) 
    
# Calculate the total width of a pair of grids
total_width = num_columns * dot_distance

# Starting x-position for the first pair of grids
start_x = -(1.5 * total_width + pair_distance)

# Starting y-position
start_y = dot_distance * (num_rows - 1) / 2

# Loop to draw three pairs of 3x3 grids
for i in range(3):
    dot_distance = 50
    draw_grid(start_x + i * (total_width + pair_distance), start_y)

# Close the Turtle graphics window on click
turtle.exitonclick()
