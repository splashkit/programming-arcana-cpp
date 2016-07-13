/// Program: HouseDrawing
///
/// This program opens a window and draws a picture of a house.
///

#include "splashkit.h"
#include "splashkit_starter.h"

/// Procedure: draw_house
///
/// This procedure draws a house by calling procedures
/// that fill a rectangle for the walls and a triangle
/// for the roof.
void draw_house()
{
    fill_rectangle(COLOR_GREY, 300, 300, 200, 200);
    fill_triangle(COLOR_RED, 250, 300, 400, 150, 550, 300);
}

/// Procedure: draw_hill
///
/// This procedure draws an ellipse that is half off the
/// bottom of the screen so that it looks like a hill.
void draw_hill()
{
    fill_ellipse(COLOR_BRIGHT_GREEN, 0, 400, 800, 400);
}

/// Procedure: main
///
/// This is where the program starts.
/// Main will open a window, then draw a hill with
/// a house on top before delaying for 5 seconds and
/// then ending.
void main()
{
    open_window("House Drawing", 800, 600);
    clear_screen(COLOR_WHITE);

    draw_hill();
    draw_house();

    refresh_screen(60);
    delay(5000);
}
