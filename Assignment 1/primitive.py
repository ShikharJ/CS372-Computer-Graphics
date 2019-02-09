# Using turtle graphics library.
from turtle import *

# Function to draw a single hexagonal side.
def draw_hexagon(side_length):
    # Begin drawing with white colour.
    pendown()
    pencolor("white")
    # Draw a line of provided length.
    forward(side_length)
    # Orient the cursor by 60 degrees.
    right(60)

# Initialization and background colour.
setup()
bgcolor("black")

# Move cursor to initial drawing position.
goto(-50, 100)

# Set the colour to fill the hexagon.
# Then draw all the sides.
fillcolor("white")
begin_fill()
for i in range(6):
    draw_hexagon(100)
end_fill()

# Exit on click.
exitonclick()