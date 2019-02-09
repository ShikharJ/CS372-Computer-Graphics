#include <stdio.h>
#include <GL/glut.h>

// Global variables for circle's coordinates and radius.
int x_center, y_center, radius;

void plot(int x, int y)
{
    // Draw the points with respect to the center.
    glBegin(GL_POINTS);
        glVertex2i(x_center + x, y_center + y);
    glEnd();
}

void display()
{
    // Set the display area colour set using glClearColor().
    glClear(GL_COLOR_BUFFER_BIT);
    // Colour fill.
    glColor3ub(255, 255, 255);
    // Set point sizes.
    glPointSize(2.0);

    // Initial parameters for points.
    int x = 0;
    int y = radius;
    int h = 1 - radius;

    // Draw the points where the circle crosses the axes.
    plot(x, y);
    plot(x, -y);
    plot(y, x);
    plot(-y, x);

    // Main part of the algorithm.
    while (y > x)
    {
        if (h < 0)
        {
            h += (2 * x) + 3;
        } else
        {
            h += (2 * (x - y)) + 5;
            y -= 1;
        }

        x += 1;

        // Plot the points in counter-clockwise fashion.
        plot(x, y);
        plot(-x, y);
        plot(-y, x);
        plot(-y, -x);
        plot(-x, -y);
        plot(x, -y);
        plot(y, -x);
        plot(y, x);
    }

    // Begin execution of the above code.
    glFlush();
}

int main(int argc, char **argv)
{
    char c;

    printf("Bresenham's Circle Drawing Algorithm\n");
    printf("Please Enter The X-Coordinate of the Center: ");
    scanf("%d%c", &x_center, &c);
    printf("Please Enter The Y-Coordinate of the Center: ");
    scanf("%d%c", &y_center, &c);
    printf("Please Enter The Radius of the Circle: ");
    scanf("%d%c", &radius, &c);

    // Initialize to the command-line arguments.
    glutInit(&argc, argv);
    // Setup the colour depth of the window buffers.
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    // Assign the position, size and name to the window.
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(640, 480);
    glutCreateWindow("Bresenham's Circle Drawing Algorithm");

    // Setup a black background.
    glClearColor(0.0, 0.0, 0.0, 0.0);
    // Setup viewing projection.
    glMatrixMode(GL_PROJECTION);
    // Initialize identity matrix.
    glLoadIdentity();
    // Setup a viewport.
    gluOrtho2D(0.0, 640.0, 0.0, 480.0);

    // Pass the display function to generate the display.
    glutDisplayFunc(display);
    // Hand over the execution to the glut library.
    glutMainLoop();

    return 0;
}
