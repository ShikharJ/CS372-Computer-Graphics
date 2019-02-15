#include <iostream>
#include <fstream>
#include <vector>
#include <GL/glut.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtx/matrix_transform_2d.hpp>

using namespace std;

// Global variables for window size, choice of transformation
// and transformation matrices.
int choice;
int max_height = 1200, max_width = 800;
vector<glm::vec4> storage;
glm::mat4 scaler = glm::scale(glm::mat4(1.0f), glm::vec3(0.5f));
glm::mat4 shearerX = glm::shearX(glm::mat3(1.0f), -0.2f);
glm::mat4 shearerY = glm::shearY(glm::mat3(1.0f), -0.2f);
glm::mat4 reflectorX = glm::scale(glm::mat4(1.0f),
        glm::vec3(1.0f, -1.0f, 1.0f));
glm::mat4 reflectorY = glm::scale(glm::mat4(1.0f),
        glm::vec3(-1.0f, 1.0f, 1.0f));
glm::mat4 rotator = glm::transpose(glm::rotate(glm::mat3(1.0f),
        3.14f));
glm::mat4 translator = glm::transpose(glm::translate(
        glm::mat4(1.0f), glm::vec3(-200.0f, -100.0f, 0.0f)));

// Function to read the file with polygon coordinates
// and store them.
void store_polygon()
{
    ifstream polygon;
    polygon.open("polygon.txt");

    if (not polygon.is_open())
    {
        cerr << "The File Cannot Be Read!" << endl;
        return ;
    }

    float x, y;

    while (polygon >> x >> y)
    {
        storage.push_back(glm::vec4(x, y, 0.0f, 1.0f));
    }

    polygon.close();
}

// Function to print the processed polygon.
void print_processed(vector<glm::vec4> &v)
{
    // Colour fill.
    glColor3ub(255, 255, 255);
    // Set point sizes.
    glPointSize(2.0);

    float x1, y1, x2, y2;

    for (auto it = v.begin(); it != v.end(); it++)
    {
        glm::vec4 coordinate = *it;

        if (it == v.begin())
        {
            x1 = coordinate[0];
            y1 = coordinate[1];
        } else
        {
            x2 = coordinate[0];
            y2 = coordinate[1];

            glBegin(GL_LINES);
                glVertex2f(x1, y1);
                glVertex2f(x2, y2);
            glEnd();

            glFlush();
            x1 = x2;
            y1 = y2;
        }
    }
}

// Function to print the original polygon.
void original()
{
    print_processed(storage);
}

// Function to scale the original polygon.
void scaling()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * scaler;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to reflect the original polygon along X axis.
void reflectionX()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * reflectorX;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to reflect the original polygon along Y axis.
void reflectionY()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * reflectorY;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to shear the original polygon along X axis.
void shearX()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * shearerX;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to shear the original polygon along Y axis.
void shearY()
{   
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * shearerY;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to rotate the original polygon counter-clockwise.
void rotation()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * rotator;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to translate the original polygon.
void translation()
{
    vector<glm::vec4> processed;

    for (auto i : storage)
    {
        i = i * translator;
        processed.push_back(i);
    }

    print_processed(processed);
}

// Function to display the drawn and transformed polygon.
void display()
{
    if (choice == 1)
    {
        original();
    } else if (choice == 2)
    {
        scaling();
    } else if (choice == 3)
    {
        reflectionX();
    } else if (choice == 4)
    {
        reflectionY();
    } else if (choice == 5)
    {
        shearX();
    } else if (choice == 6)
    {
        shearY();
    } else if (choice == 7)
    {
        rotation();
    } else
    {
        translation();
    }
}

int main(int argc, char **argv)
{
    store_polygon();

    cout << "Welcome To 2D Transformer" << endl;
    cout << "1) Original" << endl;
    cout << "2) Scaling" << endl;
    cout << "3) Reflection along X Axis" << endl;
    cout << "4) Reflection along Y Axis" << endl;
    cout << "5) Shear along X Axis" << endl;
    cout << "6) Shear along Y Axis" << endl;
    cout << "7) Rotation" << endl;
    cout << "8) Translation" << endl;
    cout << "Enter Choice: ";
    cin >> choice;

    if (choice < 1 or choice > 8){
        cout << "Wrong Input Entered! Aborting!!" << endl;
        return 0;
    }

    // Initialize to the command-line arguments.
    glutInit(&argc, argv);
    // Setup the colour depth of the window buffers.
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    // Assign the position, size and name to the window.
    glutInitWindowPosition(100, 150);
    glutInitWindowSize(max_height, max_width);
    glutCreateWindow("2D Modelling Transformation");

    // Setup a black background.
    glClearColor(0.0, 0.0, 0.0, 0.0);
    // Setup viewing projection.
    glMatrixMode(GL_PROJECTION);
    // Initialize identity matrix.
    glLoadIdentity();
    // Setup a viewport.
    gluOrtho2D(-600.0, 600.0, -400.0, 400.0);
    // Set the display area colour set using glClearColor().
    glClear(GL_COLOR_BUFFER_BIT);

    // Pass the display function to generate the display.
    glutDisplayFunc(display);
    // Hand over the execution to the glut library.
    glutMainLoop();

    return 0;
}