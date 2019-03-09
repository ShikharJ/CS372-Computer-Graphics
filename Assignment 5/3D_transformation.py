# Using turtle graphics library.
import turtle

# Set the window sizes.
max_height = 1200
max_width = 800
storage = []

# Function to print the processed polygon.
def print_processed(processed):
    x1 = processed[0][0]
    y1 = processed[0][1]
    for i in processed[1:]:
        x2 = i[0]
        y2 = i[1]
        turtle.penup()
        turtle.pencolor("white")
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        turtle.penup()
        x1 = x2
        y1 = y2

# Function to process the polygon coordinates.
def process_matrix(matrix):
    processed = []
    for i in storage:
        j = [0.0, 0.0, 0.0, 0.0]
        for a in range(len(matrix)): 
            for c in range(4): 
                j[a] += matrix[a][c] * i[c]
        processed.append(j)
    print_processed(processed)

# Function to print the original polygon.
def original():
    print_processed(storage)

# Function to scale the original polygon.
def scaling():
    scaler = [[0.5, 0.0, 0.0, 0.0],
              [0.0, 0.5, 0.0, 0.0],
              [0.0, 0.0, 0.5, 0.0],
              [0.0, 0.0, 0.0, 1.0]]
    process_matrix(scaler)

# Function to reflect the original polygon about XY plane.
def reflectionXY():
    reflectorXY = [[1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, -1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]]
    process_matrix(reflectorXY)
    
# Function to reflect the original polygon about YZ plane.
def reflectionYZ():
    reflectorYZ = [[-1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]]
    process_matrix(reflectorYZ)

# Function to reflect the original polygon about ZX axis.
def reflectionZX():
    reflectorZX = [[1.0, 0.0, 0.0, 0.0],
                  [0.0, -1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]]
    process_matrix(reflectorZX)

# Function to shear the original polygon along X axis.
def shearX():
    shearerX = [[1.0, -0.2, -0.2, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerX)

# Function to shear the original polygon along Y axis.
def shearY():
    shearerY = [[1.0, 0.0, 0.0, 0.0],
                [-0.2, 1.0, -0.2, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerY)

# Function to shear the original polygon along Z axis.
def shearZ():
    shearerZ = [[1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [-0.2, -0.2, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerZ)

# Function to shear the original polygon along XY plane.
def shearXY():
    shearerXY = [[1.0, -0.2, -0.2, 0.0],
                [-0.2, 1.0, -0.2, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerXY)

# Function to shear the original polygon along YZ plane.
def shearYZ():
    shearerYZ = [[1.0, 0.0, 0.0, 0.0],
                [-0.2, 1.0, -0.2, 0.0],
                [-0.2, -0.2, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerYZ)

# Function to shear the original polygon along ZX plane.
def shearZX():
    shearerZX = [[1.0, -0.2, -0.2, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [-0.2, -0.2, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]]
    process_matrix(shearerZX)

# Function to rotate the original polygon around X axis.
def rotationX():
    rotatorX = [[1.0, 0.0, 0.0, 0.0],
               [0.0, -1.0, 0.0, 0.0],
               [0.0, 0.0, -1.0, 0.0],
               [0.0, 0.0, 0.0, 1.0]]
    process_matrix(rotatorX)

# Function to rotate the original polygon around Y axis.
def rotationY():
    rotatorY = [[-1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0],
               [0.0, 0.0, -1.0, 0.0],
               [0.0, 0.0, 0.0, 1.0]]
    process_matrix(rotatorY)

# Function to rotate the original polygon around Z axis.
def rotationZ():
    rotatorZ = [[-1.0, 0.0, 0.0, 0.0],
               [0.0, -1.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0],
               [0.0, 0.0, 0.0, 1.0]]
    process_matrix(rotatorZ)

# Function to translate the original polygon.
def translation():
    translator = [[1.0, 0.0, 0.0, -200.0],
                  [0.0, 1.0, 0.0, -100.0],
                  [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]]
    process_matrix(translator)

# Function to read the file with polygon coordinates
# and storing them.
def draw_polygon(choice):
    with open('polygon.txt') as f:
        for line in f:
            x1, y1 = [float(x) for x in line.split()]
            storage.append([x1, y1, 0.0, 1.0])

    if choice == 1:
        original()
    elif choice == 2:
        scaling()
    elif choice == 3:
        reflectionXY()
    elif choice == 4:
        reflectionYZ()
    elif choice == 5:
        reflectionZX()
    elif choice == 6:
        shearX()
    elif choice == 7:
        shearY()
    elif choice == 8:
        shearZ()
    elif choice == 9:
        shearXY()
    elif choice == 10:
        shearYZ()
    elif choice == 11:
        shearZX()
    elif choice == 12:
        rotationX()
    elif choice == 13:
        rotationY()
    elif choice == 14:
        rotationZ()
    else:
        translation()

# Function to display the drawn and filled polygon.
def display():
    print("1) Original")
    print("2) Scaling")
    print("3) Reflection about XY Plane")
    print("4) Reflection about YZ Plane")
    print("5) Reflection about ZX Plane")
    print("6) Shear along X Axis")
    print("7) Shear along Y Axis")
    print("8) Shear along Z Axis")
    print("9) Shear along XY Plane")
    print("10) Shear along YZ Plane")
    print("11) Shear along ZX Plane")
    print("12) Rotation about X Axis")
    print("13) Rotation about Y Axis")
    print("14) Rotation about Z Axis")
    print("15) Translation")
    choice = int(input("Enter Choice: "))
    if (choice < 1 or choice > 15):
        print("Incorrect Input! Aborting!!")
        return
    draw_polygon(choice)

# Initial input.
print("3D Modelling Transformation\n")

# Initialization and background colour.
turtle.setup(max_height, max_width)
turtle.bgcolor("black")

# Set the fill colour to black.
turtle.fillcolor("black")
# Initiate the algorithm.
display()

# Exit on click.
turtle.exitonclick()