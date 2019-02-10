# Using turtle graphics library.
import turtle

# Set the window, edge table and active edge list sizes.
max_height = 1600
max_width = 1200
edge_table = [[] for i in range(max_height)]
active_edge_list = []

# Function for printing the tuples.
def print_tuples(buckets):
    if len(buckets) > 0:
        print("Count: " + str(len(buckets)))

    for i in buckets:
        print("y: " + str(i[0]) + ", x (intersection): " +
            str(i[1]) + ", dx/dy: " + str(i[2]))

# Function for printing the edge tables.
def print_table():
    count = 0
    print("Printing Edge Table:")
    for i in edge_table:
        if len(i) > 0:
            print("Scanline: " + str(count))
        print_tuples(i)
        count += 1

# Function for adding an edge to the list of buckets.
def add_edge(buckets, y, x, dx_dy):
    buckets.append([y, x, dx_dy])
    buckets.sort(key = lambda k : k[1])

# Function for removing and edge from the active edge list.
def remove_edge(buckets, y):
    i = 0
    while i < len(buckets):
        if buckets[i][0] == y:
            del buckets[i]
        else:
            i += 1

# Function for updating the active edge list.
def update_active_edge_list():
    for i in active_edge_list:
        i[1] += i[2]

# Function for storing the edges in the edge list.
def store_edge_table(x1, y1, x2, y2):
    if y1 == y2:
        return
    elif x2 == x1:
        dx_dy = 0.0
    else:
        dx_dy = (x2 - x1) / (y2 - y1)
        print("Slope string for " + str(x1) + ", " + str(y1) +
        " and " + str(x2) + ", " + str(y2) + ": " + str(dx_dy))

    if y1 > y2:
        add_edge(edge_table[y2], y1, x2, dx_dy)
    else:
        add_edge(edge_table[y1], y2, x1, dx_dy)

# Function for filling the individual pixels between two 
# intersection coordinates of the edges of the polygon
# with respect the scan line.
def scanline_fill():
    for i in range(max_height):
        for j in edge_table[i]:
            add_edge(active_edge_list, j[0], j[1], j[2])
        print_tuples(active_edge_list)
        remove_edge(active_edge_list, i)
        active_edge_list.sort(key = lambda k : k[1])
        print_tuples(active_edge_list)

        count = 0
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        flag = False

        for j in active_edge_list:
            if count % 2 == 0:
                x1 = int(j[1])
                y1 = int(j[0])
                if x1 == x2:
                    if (((x1 == y1) and (x2 != y2)) or
                        ((x1 != y1) and (x2 == y2))):
                        x2 = x1
                        y2 = y1
                    else:
                        count += 1
                else:
                    count += 1
            else:
                x2 = int(j[1])
                y2 = int(j[0])
                flag = False

                if x1 == x2:
                    if (((x1 == y1) and (x2 != y2)) or
                        ((x1 != y1) and (x2 == y2))):
                        x1 = x2
                        y1 = y2
                    else:
                        flag = True
                        count += 1
                else:
                    flag = True
                    count += 1

                if flag == True:
                    turtle.pencolor("white")
                    turtle.goto(x1, i)
                    turtle.pendown()
                    turtle.goto(x2, i)
                    turtle.penup()

        update_active_edge_list()
    print("Scanline Filling Complete")

# Function to read the file with polygon coordinates
# and insert them into the edge table, and drawing the polygon.
def draw_polygon():
    with open('polygon.txt') as f:
        x1, y1 = [int(x) for x in next(f).split()]
        print("Storing Edges In Table:")
        for line in f:
            x2, y2 = [int(x) for x in line.split()]
            turtle.penup()
            turtle.pencolor("white")
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.goto(x2, y2)
            turtle.penup()
            store_edge_table(x1, y1, x2, y2)
            x1 = x2
            y1 = y2

# Function to display the drawn and filled polygon.
def display():
    draw_polygon()
    print_table()
    scanline_fill()

# Initial input.
print("Scan Line Polygon Filling Algorithm\n")

# Initialization and background colour.
turtle.setup(max_height, max_width)
turtle.bgcolor("black")

# Set the fill colour to black.
turtle.fillcolor("black")
# Initiate the algorithm.
display()

# Exit on click.
turtle.exitonclick()