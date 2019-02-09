#include <stdio.h>
#include <GL/glut.h>

void display()
{
    // Set the display area to the colour set using glClearColor().
    glClear(GL_COLOR_BUFFER_BIT);
    // Colour fill.
    glColor3f(1.0, 1.0, 1.0);
    // Draw the polygon counter-clockwise.
    glBegin(GL_POLYGON);
        glVertex3f(4.0, 4.0, 0.0);
        glVertex3f(6.0, 4.0, 0.0);
        glVertex3f(7.0, 6.0, 0.0);
        glVertex3f(6.0, 8.0, 0.0);
        glVertex3f(4.0, 8.0, 0.0);
        glVertex3f(3.0, 6.0, 0.0);
    glEnd();
    // Begin execution of the above code.
    glFlush();
}

int main(int argc, char **argv)
{
    // Initialize to the command-line arguments.
    glutInit(&argc, argv);
    // Setup the colour depth of the window buffers.
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    // Assign the position, size and name to the window.
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Hexagon");

    // Setup a black background.
    glClearColor(0.0, 0.0, 0.0, 0.0);
    // Setup viewing projection.
    glMatrixMode(GL_PROJECTION);
    // Initialize identity matrix.
    glLoadIdentity();
    // Setup a 10x10x2 view.
    glOrtho(0.0, 10.0, 0.0, 10.0, -1.0, 1.0);

    // Pass the display function to generate the display.
    glutDisplayFunc(display);
    // Hand over the execution to the glut library.
    glutMainLoop();

    return 0;
}