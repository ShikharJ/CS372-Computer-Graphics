# Using turtle graphics library.
import turtle

# Function to draw a single point.
def draw_point(x_center, y_center, x, y):
    turtle.goto(x_center + x, y_center + y)
    turtle.dot(5, "white")

# Function to draw the whole circle.
def draw_circle(x_center, y_center, radius):

    # Initial arguments.
    x_center = int(x_center)
    y_center = int(y_center)
    x = int(0)
    y = int(radius)
    h = int(1 - y)

    # Draw the points where the circle crosses the axes.
    draw_point(x_center, y_center, x, y);
    draw_point(x_center, y_center, x, -y);
    draw_point(x_center, y_center, y, x);
    draw_point(x_center, y_center, -y, x);

    # Main part of the algorithm.
    while y > x:
        if h < 0:
            h += (2 * x) + 3;
        else:
            h += (2 * (x - y)) + 5;
            y -= 1;

        x += 1;

        # Plot the points in counter-clockwise fashion.
        draw_point(x_center, y_center, x, y);
        draw_point(x_center, y_center, -x, y);
        draw_point(x_center, y_center, -y, x);
        draw_point(x_center, y_center, -y, -x);
        draw_point(x_center, y_center, -x, -y);
        draw_point(x_center, y_center, x, -y);
        draw_point(x_center, y_center, y, -x);
        draw_point(x_center, y_center, y, x);

# Initial input.
print("Bresenham's Circle Drawing Algorithm\n")
x_center = input("Please Enter The X-Coordinate of the Center: ")
y_center = input("Please Enter The Y-Coordinate of the Center: ")
radius = input("Please Enter The Radius of the Circle: ")

# Initialization and background colour.
turtle.setup()
turtle.bgcolor("black")

# Set the fill colour to black/
turtle.fillcolor("black")
# Draw the circle.
draw_circle(x_center, y_center, radius)

# Exit on click.
turtle.exitonclick()